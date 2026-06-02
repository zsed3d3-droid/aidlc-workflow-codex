# Game UI Design Movements

Use for game HUDs, mobile/tablet game shells, in-game menus, card battlers, RPG/MMO interfaces, casual games, and diegetic/FUI surfaces.

## Movement Entries

### Diegetic UI

- Definition: UI exists inside the game world as physical or in-fiction objects perceived by character and player.
- Visual cues: In-world maps, suit health lights, weapon ammo displays, watches, clipboards, physical instruments.
- Best fit: Immersive survival, horror, simulation, first-person exploration, world-heavy games.
- Use carefully / avoid: Avoid when players need fast dense state comparison or accessibility overlays.
- Request UI rationale hints: Choose when immersion and world believability matter more than HUD efficiency; tradeoff is lower scan speed.

### Spatial UI

- Definition: UI is anchored in 3D space rather than fixed to the screen overlay.
- Visual cues: AR navigation lines, floating nameplates, damage numbers, object-attached markers, spatial menus.
- Best fit: Open-world, tactical, AR-like, co-op, and 3D navigation-heavy games.
- Use carefully / avoid: Avoid visual clutter, occlusion, and camera-angle ambiguity.
- Request UI rationale hints: Choose when information must relate to locations or objects; tradeoff is depth/occlusion complexity.

### Meta UI

- Definition: Character state appears as screen-level sensory effects rather than explicit gauges.
- Visual cues: Blood edges, blur, vignettes, tinnitus, breathing, impact distortion, saturation shifts.
- Best fit: Shooters, horror, action, and cinematic survival games.
- Use carefully / avoid: Avoid replacing all precise indicators when strategy or accessibility requires exact values.
- Request UI rationale hints: Choose when bodily feedback and tension matter; tradeoff is imprecision and accessibility risk.

### Skeuomorphic Skinned UI

- Definition: Genre-themed textures and materials skin menus, frames, or controls.
- Visual cues: Stone, leather, parchment, metal, gothic frames, carved borders, fantasy ornaments.
- Best fit: Fantasy RPG, MMORPG, dungeon crawlers, historical strategy, themed inventory screens.
- Use carefully / avoid: Avoid overdecorated panels that reduce text clarity or touch precision.
- Request UI rationale hints: Choose when genre atmosphere must carry into menus; tradeoff is visual weight.

### Cyberpunk HUD / High-Tech FUI

- Definition: Fictional high-tech interface inspired by sci-fi lenses, cockpits, scans, and tactical overlays.
- Visual cues: Neon cyan/orange/red, wireframes, radar, data grids, monospaced labels, glitch/noise.
- Best fit: Cyberpunk, mecha, hacking, tactical sci-fi, scanner-heavy games.
- Use carefully / avoid: Avoid busy overlays that hide gameplay or fail contrast checks.
- Request UI rationale hints: Choose when the UI should feel like a device or cybernetic layer; tradeoff is noise and fatigue.

### Minimalist Abstraction / Flat Hyper-HUD

- Definition: Minimal game UI using clean typography, thin lines, muted surfaces, and sparse indicators.
- Visual cues: Thin bars, simple minimaps, translucent black panels, clean sans labels, neutral palettes.
- Best fit: Modern action, racing, open-world, art games, and screen-space-sensitive play.
- Use carefully / avoid: Avoid stripping away affordances needed for complex systems.
- Request UI rationale hints: Choose when gameplay visuals should dominate; tradeoff is less genre flavor.

### Y2K Pop-Punk / Street Punk UI

- Definition: Rebellious collage UI from graffiti, street culture, comic print, punk layouts, and diagonal motion.
- Visual cues: Red/black/white contrast, diagonal grids, halftone dots, brush/spray textures, distorted 3D type.
- Best fit: Stylish RPGs, fighting games, street sports, youth-culture action games.
- Use carefully / avoid: Avoid for quiet strategy, serious simulation, or text-heavy menus.
- Request UI rationale hints: Choose when attitude and instant identity are core; tradeoff is higher visual chaos.

### Casual Juicy / Jelly Style

- Definition: High-feedback casual/mobile UI built around bouncy, glossy, dopamine-rich interactions.
- Visual cues: Large rounded buttons, shiny gradients, bounce transitions, reward bursts, candy/plastic surfaces.
- Best fit: Match-3, idle, tycoon, reward shops, casual event popups.
- Use carefully / avoid: Avoid serious strategy, horror, and low-distraction puzzle screens.
- Request UI rationale hints: Choose when tap delight and reward collection matter; tradeoff is low seriousness.

### Subculture Anime Flat / Tech-Aesthetic

- Definition: Anime-character-first UI with flat tech panels, thin strokes, diagonal grids, and restrained sci-fi cues.
- Visual cues: Clean flat surfaces, thin outlines, angular panels, mono indicators, subtle glitch/noise.
- Best fit: Gacha RPG, character collection, anime strategy, visual-novel-adjacent systems.
- Use carefully / avoid: Avoid letting chrome compete with character art.
- Request UI rationale hints: Choose when 2D character art must remain the hero; tradeoff is high asset dependency.

### Hyper-Casual Hybrid Minimalism

- Definition: Ultra-low-cognitive-load UI for games players understand in under a second.
- Visual cues: Minimal HUD, dynamic-only prompts, one or two bright colors, simple icons, directional layouts.
- Best fit: Hyper-casual arcade, simple puzzle, runner, merge, physics toys.
- Use carefully / avoid: Avoid for deep progression, economy, or RPG systems.
- Request UI rationale hints: Choose when instant comprehension matters; tradeoff is limited depth expression.

### Card-Battler Diegetic Layering

- Definition: Mobile-first card UI that treats digital cards as layered hand-held objects.
- Visual cues: Thumb-reachable card rows, drag-to-play motion, rarity frames, holographic effects, deck layering.
- Best fit: Card battlers, TCG/CCG, hero battlers, one-hand portrait combat.
- Use carefully / avoid: Avoid when card state is too dense for small portrait layouts.
- Request UI rationale hints: Choose when physical card manipulation drives play; tradeoff is animation/state complexity.

### Liquid Glassmorphic Game-HUD

- Definition: High-end translucent game HUD using liquid glass and blurred panels over 3D scenes.
- Visual cues: Blur panels, moving reflections, liquid gradients, gyro-like light response, translucent menus.
- Best fit: Premium mobile RPG/MMO lobbies, equipment, settings, high-fidelity 3D games.
- Use carefully / avoid: Contrast, performance, and background-readability risk.
- Request UI rationale hints: Choose when menus must feel premium without hiding 3D art; tradeoff is GPU/accessibility cost.

### Retro Pixel Chiptune UI

- Definition: Pixel-era game UI built from bitmap type, grid components, scanlines, and choppy animation.
- Visual cues: Pixel art panels, bitmap fonts, CRT filters, low-frame animation, handheld-console frames.
- Best fit: Indie RPG, idle pixel games, retro arcade, nostalgia-driven games.
- Use carefully / avoid: Avoid tiny unreadable bitmap text on mobile.
- Request UI rationale hints: Choose when nostalgia and fandom matter; tradeoff is readability/responsiveness.

### Hard-SciFi Diegetic FUI

- Definition: Command-room style sci-fi UI for large strategic or mechanical systems.
- Visual cues: Dense multi-grid panels, monospaced data, thin borders, muted dark layers, tactical readouts.
- Best fit: Space 4X, mecha command, tablet strategy, fleet management.
- Use carefully / avoid: Avoid overwhelming casual players or small phones.
- Request UI rationale hints: Choose when intellectual command immersion matters; tradeoff is high density.

### Skeuomorphic Tactical Command

- Definition: Tactical UI mimicking physical military, medieval, or command-table objects.
- Visual cues: Metal monitors, radar scopes, parchment maps, leather, switches, dials, document-folder motions.
- Best fit: Military strategy, historical war, siege, tactical simulation.
- Use carefully / avoid: Avoid when fast modern scanning beats atmosphere.
- Request UI rationale hints: Choose when command fantasy is central; tradeoff is heavier visuals.

### Modular Dashboard Minimalism

- Definition: Game management UI combining web dashboards with simulation data surfaces.
- Visual cues: Bento grids, charts, tables, sidebars, detail panels, low decoration.
- Best fit: Sports management, tycoon, strategy economy, simulation admin screens.
- Use carefully / avoid: Avoid if the core game loop is action or emotion-led.
- Request UI rationale hints: Choose when data drives decisions; tradeoff is less cinematic atmosphere.

### Skeuomorphic Skinned MMORPG

- Definition: Dense RPG/MMO edge UI with themed skill slots, minimaps, party state, and quest trackers.
- Visual cues: Gold/rune frames, edge-packed controls, multi-tier skill pads, ornate quick slots.
- Best fit: Hardcore mobile MMORPG, action RPG, fantasy combat.
- Use carefully / avoid: Avoid obscuring combat view or shrinking tap targets.
- Request UI rationale hints: Choose when players expect many persistent combat controls; tradeoff is clutter.

### Skeuomorphic Diegetic Hearth

- Definition: Board/card game UI that makes the screen feel like a physical tabletop.
- Visual cues: Wood/stone top-down surfaces, floating cards/tokens, dice boxes, board objects as menu controls.
- Best fit: Digital board games, CCG, Hearthstone-like battlers, tabletop adaptations.
- Use carefully / avoid: Avoid when compact competitive clarity matters more than tabletop feel.
- Request UI rationale hints: Choose when physical table presence is part of fun; tradeoff is heavy scene composition.

### Geometry Primitive Minimalism

- Definition: Game UI and objects unified through primitive shapes, flat planes, and minimal color.
- Visual cues: Circles/squares/triangles, thin grids, monochrome base, one accent color, object/UI shape consistency.
- Best fit: Minimal arcade, 2048-like puzzles, hyper-casual, abstract action.
- Use carefully / avoid: Avoid for narrative or character-heavy games.
- Request UI rationale hints: Choose when rule clarity matters above theme; tradeoff is low atmosphere.

### Flat Cartoonish / Vector Playful

- Definition: Friendly vector UI lowering entry barriers with cartoon simplicity.
- Visual cues: Bold strokes or no strokes, flat colors, rounded toy-like components, chunky type.
- Best fit: Party games, casual puzzles, family games, hidden-object, social games.
- Use carefully / avoid: Avoid when the game needs tension, realism, or premium seriousness.
- Request UI rationale hints: Choose when approachability and instant charm matter; tradeoff is reduced depth.

### Low-Poly Cozy Naturalism

- Definition: Warm low-poly/minimal 3D UI for cozy, idle, and healing games.
- Visual cues: Low-poly objects, pastel matte colors, miniature lighting, rounded sans type, natural ambience.
- Best fit: Cozy idle, tycoon, pet/cat games, garden/town builders.
- Use carefully / avoid: Avoid high-precision competitive or tactical surfaces.
- Request UI rationale hints: Choose when relaxation and collection reward matter; tradeoff is lower information density.

### Monochrome Silhouette

- Definition: Artistic high-contrast UI using silhouettes and backlight to focus on movement and timing.
- Visual cues: Black silhouettes, bright backgrounds, minimal text/numbers, shadow-theater composition.
- Best fit: Atmospheric platformers, minimal action, timing puzzles, art games.
- Use carefully / avoid: Avoid dense inventory, RPG stats, or color-coded systems.
- Request UI rationale hints: Choose when motion readability and mood matter; tradeoff is limited UI vocabulary.
