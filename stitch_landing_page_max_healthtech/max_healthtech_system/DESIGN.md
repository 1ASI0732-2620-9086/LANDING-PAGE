---
name: MAX HealthTech System
colors:
  surface: '#f8f9ff'
  surface-dim: '#ccdbf1'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eef4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dbe9ff'
  surface-container-highest: '#d5e4fa'
  on-surface: '#0e1c2d'
  on-surface-variant: '#424753'
  inverse-surface: '#233142'
  inverse-on-surface: '#eaf1ff'
  outline: '#727785'
  outline-variant: '#c2c6d5'
  surface-tint: '#005bc0'
  primary: '#0058bb'
  on-primary: '#ffffff'
  primary-container: '#2571df'
  on-primary-container: '#fefcff'
  inverse-primary: '#adc6ff'
  secondary: '#005fb0'
  on-secondary: '#ffffff'
  secondary-container: '#4e9dff'
  on-secondary-container: '#003364'
  tertiary: '#005f9c'
  on-tertiary: '#ffffff'
  tertiary-container: '#1779c0'
  on-tertiary-container: '#fdfcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#d5e3ff'
  secondary-fixed-dim: '#a6c8ff'
  on-secondary-fixed: '#001c3b'
  on-secondary-fixed-variant: '#004787'
  tertiary-fixed: '#d0e4ff'
  tertiary-fixed-dim: '#9bcbff'
  on-tertiary-fixed: '#001d34'
  on-tertiary-fixed-variant: '#004a7a'
  background: '#f8f9ff'
  on-background: '#0e1c2d'
  surface-variant: '#d5e4fa'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.03em
  display-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 26px
    fontWeight: '600'
    lineHeight: 34px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
    letterSpacing: -0.005em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: '0'
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.03em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 2.5rem
  margin-mobile: 1.25rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system expresses a forward-thinking, clinical-grade digital health experience. It diverges entirely from conventional medical tropes—discarding stark clinical whites, literal cross motifs, and sterilized laboratory aesthetics in favor of a deep, luminous digital workspace engineered for precision, focus, and cognitive calm.

### Personality & Demographics
- **Target Audience:** Healthcare practitioners, biotech researchers, clinical administrators, and patients interacting with high-trust telemetry dashboards.
- **Tone:** Methodical, hyper-credible, technologically advanced, and profoundly empathetic.
- **Visual Movement:** High-end SaaS Precision mixed with Soft Ambient Minimalist depth. The interface utilizes multi-stop cerulean gradients, soft luminous surfaces, refined hairline borders, and generous atmospheric whitespace to reduce clinical charting fatigue.

## Colors

The color architecture is built around layered shades of deep marine and luminous cerulean tones, preventing stark visual contrast while preserving legibility.

### Core Palette Tokens
- **Primary Strong:** `#2F78E6` (Key actions, dominant interactive triggers, active navigation indicators)
- **Primary Light:** `#5AA9F3` (Hover states, focal highlights, secondary metric badges)
- **Secondary Bright:** `#4F9DFF` (Accent tags, secondary buttons, interactive micro-states)
- **Secondary Soft:** `#6FB0FF` (Tonal outlines, subtle state indicators)
- **Deep Navy / Ink Neutral:** `#0B1A2A` (Primary text, dark surface foundations, high-emphasis icons)
- **Medium Dark Slate:** `#1A3552` (Secondary text in light mode, tertiary borders in dark mode)
- **Soft Azure Wash:** `#D8ECFF` (Chip backgrounds, selected table rows, hover overlays)
- **Ultra-Light Ice Canvas:** `#F2F7FF` (Primary light canvas background)
- **Subtle Azure Border:** `#DBE7F6` (Default structural borders, divider hairlines)

### Dark Mode & Surface Panels
- **Panel Base:** `#0F2033` (Card containers, structural app sidebars in dark context)
- **Panel Raised:** `#13263B` (Elevated modals, popovers, dropdown containers)

### Structural Gradients
- **Light Atmosphere Gradient:** `linear-gradient(180deg, #F7FBFF 0%, #EEF5FF 100%)` (Page backgrounds, hero metric cards)
- **Dark Telemetry Gradient:** `linear-gradient(180deg, #122840 0%, #0D1C2F 100%)` (Dark mode headers, patient telemetry monitors)

## Typography

The type scale combines **Plus Jakarta Sans** for prominent navigational, editorial, and headline surfaces with **Inter** for dense analytical telemetry, patient notes, and operational inputs.

- **Plus Jakarta Sans** injects architectural clarity, structural geometry, and contemporary digital confidence.
- **Inter** provides neutral, high x-height tracking that ensures zero ambiguity across alphanumeric vitals, numerical lab units, and pharmaceutical data.
- Numbers in clinical readouts must always employ tabular lining figures (`font-feature-settings: 'tnum' on, 'cv05' on`) to ensure absolute alignment across vertically aligned data sets.

## Layout & Spacing

This design system uses a strict **8pt computational rhythm** overlaid on a 12-column fluid grid.

### Breakpoints & Canvas Geometry
- **Desktop (1440px+):** 12 columns, 24px gutters (`1.5rem`), dynamic canvas margin (`2.5rem` min). Fluid main stage anchored by a collapsible 280px navigation spine.
- **Tablet (768px - 1023px):** 8 columns, 16px gutters (`1rem`), 24px canvas margins. Auxiliary telemetry panels fold into modular slide-overs.
- **Mobile (320px - 767px):** 4 columns, 16px gutters, 20px margins (`1.25rem`). Cards drop internal horizontal splitting and stack into single-column modules.

### Internal Spacing Rhythm
- Compact widgets (e.g., metric counters, quick toggles) prioritize high visual density with `space-sm` and `space-md`.
- Analytical workspaces utilize `space-lg` to create distinct boundary isolation between charts and patient records, eliminating operational noise.

## Elevation & Depth

Depth is established through soft, multi-tier atmospheric ambient shadowing combined with structural hairline borders (`1px solid #DBE7F6`). Hard drop shadows are strictly prohibited.

### Tonal Shadows
- **Level 1 (Subtle SaaS Resting):** `box-shadow: 0 1px 3px rgba(11, 26, 42, 0.04), 0 4px 12px rgba(47, 120, 230, 0.05);` (Standard cards, stat containers, input containers).
- **Level 2 (Hover / Active State):** `box-shadow: 0 4px 8px rgba(11, 26, 42, 0.04), 0 12px 24px rgba(47, 120, 230, 0.08);` (Interactive cards, active table rows).
- **Level 3 (Floating Overlays / Modals):** `box-shadow: 0 12px 32px rgba(11, 26, 42, 0.08), 0 24px 60px rgba(47, 120, 230, 0.12);` (Diagnostic modals, context menus).

### Glass & Backdrop Physics
For floating command bars and elevated health trackers, apply a frosted translucent surface:
- **Light Surface Backdrop:** `background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(16px); border: 1px solid #DBE7F6;`
- **Dark Surface Backdrop:** `background: rgba(15, 32, 51, 0.85); backdrop-filter: blur(16px); border: 1px solid #1A3552;`

## Shapes

The shape hierarchy establishes a balanced architectural form using generous radii (16px to 24px) for structural blocks and pill geometry for status indicators:

- **Outer Enclosures & Modals (`rounded-xl`):** `24px` (1.5rem) corner curvature for high-level viewport containers, modal dialogs, and parent dashboard panels.
- **Standard Cards & Data Modules (`rounded-lg`):** `16px` (1rem) curvature across individual insight cards, chart containers, and tables.
- **Controls & Form Elements (`rounded`):** `8px` (0.5rem) on input fields, dropdown triggers, and operational actions to preserve ergonomic click targets.
- **Micro Tags & Vital Chips:** Pill-shaped (`9999px`) for quick-scan patient states, status monitors, and contextual filters.

## Components

### Buttons
- **Primary:** Background `#2F78E6`, text `#FFFFFF`, border `none`, radius `8px` to `12px`. Hover shifts to `#5AA9F3` with smooth `150ms ease-out` transition. Shadow uses Level 1 colored glow (`0 2px 8px rgba(47, 120, 230, 0.3)`).
- **Secondary:** Background `#F2F7FF`, text `#2F78E6`, border `1px solid #DBE7F6`. Hover triggers background `#D8ECFF`.
- **Ghost / Tertiary:** Background transparent, text `#1A3552`. Hover triggers `#F2F7FF` with text `#2F78E6`.

### Form Inputs & Select Fields
- Base background `#FFFFFF`, border `1px solid #DBE7F6`, radius `8px`, text `#0B1A2A`.
- Placeholder text in `#1A3552` at 60% opacity.
- Focus state: Border transitions to `#2F78E6` accompanied by a distinct 3px focus ring `rgba(47, 120, 230, 0.15)`.

### Cards & Analytical Modules
- Default state: Background `linear-gradient(180deg, #F7FBFF 0%, #EEF5FF 100%)`, border `1px solid #DBE7F6`, radius `16px` (`rounded-lg`), padding `space-lg`.
- Embedded metric cards use deep navy typography (`#0B1A2A`) with micro-labels in medium slate (`#1A3552`).

### Chips & Badges
- Pill-shaped (`9999px`), padding `4px 12px`, font `label-md`.
- Normal/Stable Vitals: Background `#D8ECFF`, text `#2F78E6`, border `1px solid rgba(47, 120, 230, 0.2)`.
- Neutral Filters: Background `#FFFFFF`, text `#1A3552`, border `1px solid #DBE7F6`.

### Checkboxes & Radios
- Size: 18px by 18px. Unchecked state: Background `#FFFFFF`, border `1.5px solid #DBE7F6`, radius `4px` (checkbox) or `50%` (radio).
- Checked state: Background `#2F78E6`, border-color `#2F78E6`, check icon crisp white with optical center alignment.

### Specialized HealthTech Component: Telemetry Monitor Strip
- Horizontal strip container with Dark Gradient background (`#122840` to `#0D1C2F`), radius `16px`, border `1px solid #1A3552`.
- Text utilizes mono-spaced numerals (`Inter` tabular numbers) in `#D8ECFF`, with real-time waveform sparklines rendered in `#5AA9F3` and `#4F9DFF`.