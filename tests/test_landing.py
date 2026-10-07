"""Contratos del sitio HTML académico; nunca consulta el backend publicado."""
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import unittest
from urllib.parse import unquote, urlsplit
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.elements = []
        self.title = ""
        self.in_title = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


class LandingContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document = Document((ROOT / "index.html").read_text(encoding="utf-8-sig"))
        cls.references = [
            value
            for _, attrs in cls.document.elements
            for key in ("href", "src")
            if (value := attrs.get(key))
        ]

    def test_spanish_document_has_title_and_mobile_viewport(self):
        self.assertTrue(self.document.title.strip())
        html = next(attrs for tag, attrs in self.document.elements if tag == "html")
        self.assertEqual(html.get("lang"), "es")
        viewport = next(attrs for tag, attrs in self.document.elements
                        if tag == "meta" and attrs.get("name") == "viewport")
        self.assertIn("width=device-width", viewport.get("content", ""))

    def test_section_identifiers_are_unique(self):
        identifiers = [attrs["id"] for _, attrs in self.document.elements if "id" in attrs]
        self.assertTrue(identifiers)
        self.assertEqual(len(identifiers), len(set(identifiers)))

    def test_navigation_fragments_have_existing_targets(self):
        identifiers = {attrs["id"] for _, attrs in self.document.elements if "id" in attrs}
        fragments = [unquote(ref[1:]) for ref in self.references if ref.startswith("#") and ref != "#"]
        self.assertTrue(fragments)
        for fragment in fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, identifiers)

    def test_local_references_resolve_inside_the_site(self):
        local = [ref for ref in self.references if not urlsplit(ref).scheme and not ref.startswith("#")]
        self.assertTrue(local)
        for ref in local:
            with self.subTest(reference=ref):
                self.assertFalse(ref.startswith(("/", "//")), "Debe respetar el prefijo de GitHub Pages")
                path = (ROOT / unquote(urlsplit(ref).path)).resolve()
                self.assertTrue(path.is_relative_to(ROOT))
                self.assertTrue(path.is_file(), f"Recurso local inexistente: {ref}")

    def test_external_references_use_https(self):
        for ref in self.references:
            if urlsplit(ref).scheme:
                with self.subTest(reference=ref):
                    self.assertEqual(urlsplit(ref).scheme, "https")

    def test_all_max_entry_links_share_the_authentication_destination(self):
        entries = [attrs["href"] for tag, attrs in self.document.elements
                   if tag == "a" and urlsplit(attrs.get("href", "")).netloc == "max-dev-front.pages.dev"]
        self.assertGreaterEqual(len(entries), 2)
        self.assertEqual(set(entries), {"https://max-dev-front.pages.dev/auth"})

    def test_static_entry_and_assets_are_served_under_a_project_prefix(self):
        class Handler(SimpleHTTPRequestHandler):
            def do_GET(self):
                if not self.path.startswith("/LANDING-PAGE/"):
                    self.send_error(404)
                    return
                self.path = self.path.removeprefix("/LANDING-PAGE")
                super().do_GET()

            def log_message(self, *_):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), partial(Handler, directory=str(ROOT)))
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            paths = ["index.html"] + [ref for ref in self.references
                                      if not urlsplit(ref).scheme and not ref.startswith("#")]
            for path in paths:
                with self.subTest(path=path), urlopen(
                    f"http://127.0.0.1:{server.server_port}/LANDING-PAGE/{path}", timeout=5
                ) as response:
                    self.assertEqual(response.status, 200)
                    self.assertTrue(response.read())
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
