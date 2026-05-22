# Game UI 디자인 사조

Game HUD, mobile/tablet game shell, in-game menu, card battler, RPG/MMO interface, casual game, diegetic/FUI surface에 사용한다.

## Movement Entries

### Diegetic UI

- Definition: UI가 character와 player가 인식하는 physical 또는 in-fiction object로 game world 안에 존재한다.
- Visual cues: in-world map, suit health light, weapon ammo display, watch, clipboard, physical instrument.
- Best fit: Immersive survival, horror, simulation, first-person exploration, world-heavy game.
- Use carefully / avoid: player가 빠르게 dense state comparison이나 accessibility overlay를 필요로 하면 피한다.
- Request UI rationale hints: immersion과 world believability가 HUD efficiency보다 중요할 때 선택한다. tradeoff는 scan speed 감소.

### Spatial UI

- Definition: UI가 fixed screen overlay가 아니라 3D space에 anchor된다.
- Visual cues: AR navigation line, floating nameplate, damage number, object-attached marker, spatial menu.
- Best fit: Open-world, tactical, AR-like, co-op, 3D navigation-heavy game.
- Use carefully / avoid: visual clutter, occlusion, camera-angle ambiguity를 피한다.
- Request UI rationale hints: information이 location/object와 관계를 가져야 할 때 선택한다. tradeoff는 depth/occlusion complexity.

### Meta UI

- Definition: character state가 explicit gauge 대신 screen-level sensory effect로 나타난다.
- Visual cues: blood edge, blur, vignette, tinnitus, breathing, impact distortion, saturation shift.
- Best fit: Shooter, horror, action, cinematic survival game.
- Use carefully / avoid: strategy 또는 accessibility가 exact value를 요구할 때 모든 precise indicator를 대체하지 않는다.
- Request UI rationale hints: bodily feedback과 tension이 중요할 때 선택한다. tradeoff는 imprecision과 accessibility risk.

### Skeuomorphic Skinned UI

- Definition: genre-themed texture/material이 menu, frame, control을 skinning한다.
- Visual cues: stone, leather, parchment, metal, gothic frame, carved border, fantasy ornament.
- Best fit: Fantasy RPG, MMORPG, dungeon crawler, historical strategy, themed inventory screen.
- Use carefully / avoid: text clarity 또는 touch precision을 떨어뜨리는 overdecorated panel을 피한다.
- Request UI rationale hints: genre atmosphere가 menu까지 이어져야 할 때 선택한다. tradeoff는 visual weight.

### Cyberpunk HUD / High-Tech FUI

- Definition: sci-fi lens, cockpit, scan, tactical overlay에서 영감을 받은 fictional high-tech interface.
- Visual cues: neon cyan/orange/red, wireframe, radar, data grid, monospaced label, glitch/noise.
- Best fit: Cyberpunk, mecha, hacking, tactical sci-fi, scanner-heavy game.
- Use carefully / avoid: gameplay를 가리거나 contrast check에 실패하는 busy overlay를 피한다.
- Request UI rationale hints: UI가 device 또는 cybernetic layer처럼 느껴져야 할 때 선택한다. tradeoff는 noise와 fatigue.

### Minimalist Abstraction / Flat Hyper-HUD

- Definition: clean typography, thin line, muted surface, sparse indicator를 쓰는 minimal game UI.
- Visual cues: thin bar, simple minimap, translucent black panel, clean sans label, neutral palette.
- Best fit: Modern action, racing, open-world, art game, screen-space-sensitive play.
- Use carefully / avoid: complex system에 필요한 affordance까지 제거하지 않는다.
- Request UI rationale hints: gameplay visual이 우선이어야 할 때 선택한다. tradeoff는 genre flavor 감소.

### Y2K Pop-Punk / Street Punk UI

- Definition: graffiti, street culture, comic print, punk layout, diagonal motion에서 온 rebellious collage UI.
- Visual cues: red/black/white contrast, diagonal grid, halftone dot, brush/spray texture, distorted 3D type.
- Best fit: Stylish RPG, fighting game, street sport, youth-culture action game.
- Use carefully / avoid: quiet strategy, serious simulation, text-heavy menu에는 피한다.
- Request UI rationale hints: attitude와 즉각적인 identity가 core일 때 선택한다. tradeoff는 visual chaos 증가.

### Casual Juicy / Jelly Style

- Definition: bouncy, glossy, dopamine-rich interaction 중심의 high-feedback casual/mobile UI.
- Visual cues: large rounded button, shiny gradient, bounce transition, reward burst, candy/plastic surface.
- Best fit: Match-3, idle, tycoon, reward shop, casual event popup.
- Use carefully / avoid: serious strategy, horror, low-distraction puzzle screen에는 피한다.
- Request UI rationale hints: tap delight와 reward collection이 중요할 때 선택한다. tradeoff는 낮은 seriousness.

### Subculture Anime Flat / Tech-Aesthetic

- Definition: flat tech panel, thin stroke, diagonal grid, restrained sci-fi cue를 쓰는 anime-character-first UI.
- Visual cues: clean flat surface, thin outline, angular panel, mono indicator, subtle glitch/noise.
- Best fit: Gacha RPG, character collection, anime strategy, visual-novel-adjacent system.
- Use carefully / avoid: chrome이 character art와 경쟁하지 않게 한다.
- Request UI rationale hints: 2D character art가 hero로 남아야 할 때 선택한다. tradeoff는 high asset dependency.

### Hyper-Casual Hybrid Minimalism

- Definition: player가 1초 안에 이해하는 game을 위한 ultra-low-cognitive-load UI.
- Visual cues: minimal HUD, dynamic-only prompt, one/two bright colors, simple icon, directional layout.
- Best fit: Hyper-casual arcade, simple puzzle, runner, merge, physics toy.
- Use carefully / avoid: deep progression, economy, RPG system에는 피한다.
- Request UI rationale hints: instant comprehension이 중요할 때 선택한다. tradeoff는 제한된 depth expression.

### Card-Battler Diegetic Layering

- Definition: digital card를 layered hand-held object처럼 다루는 mobile-first card UI.
- Visual cues: thumb-reachable card row, drag-to-play motion, rarity frame, holographic effect, deck layering.
- Best fit: Card battler, TCG/CCG, hero battler, one-hand portrait combat.
- Use carefully / avoid: card state가 small portrait layout에 너무 dense하면 피한다.
- Request UI rationale hints: physical card manipulation이 play를 이끌 때 선택한다. tradeoff는 animation/state complexity.

### Liquid Glassmorphic Game-HUD

- Definition: 3D scene 위에 liquid glass와 blurred panel을 얹는 high-end translucent game HUD.
- Visual cues: blur panel, moving reflection, liquid gradient, gyro-like light response, translucent menu.
- Best fit: Premium mobile RPG/MMO lobby, equipment, settings, high-fidelity 3D game.
- Use carefully / avoid: contrast, performance, background-readability risk를 관리한다.
- Request UI rationale hints: menu가 3D art를 숨기지 않으면서 premium해야 할 때 선택한다. tradeoff는 GPU/accessibility cost.

### Retro Pixel Chiptune UI

- Definition: bitmap type, grid component, scanline, choppy animation으로 구성된 pixel-era game UI.
- Visual cues: pixel art panel, bitmap font, CRT filter, low-frame animation, handheld-console frame.
- Best fit: Indie RPG, idle pixel game, retro arcade, nostalgia-driven game.
- Use carefully / avoid: mobile에서 tiny unreadable bitmap text를 피한다.
- Request UI rationale hints: nostalgia와 fandom이 중요할 때 선택한다. tradeoff는 readability/responsiveness.

### Hard-SciFi Diegetic FUI

- Definition: large strategic/mechanical system을 위한 command-room style sci-fi UI.
- Visual cues: dense multi-grid panel, monospaced data, thin border, muted dark layer, tactical readout.
- Best fit: Space 4X, mecha command, tablet strategy, fleet management.
- Use carefully / avoid: casual player나 small phone을 압도하지 않는다.
- Request UI rationale hints: intellectual command immersion이 중요할 때 선택한다. tradeoff는 high density.

### Skeuomorphic Tactical Command

- Definition: physical military, medieval, command-table object를 모방하는 tactical UI.
- Visual cues: metal monitor, radar scope, parchment map, leather, switch, dial, document-folder motion.
- Best fit: Military strategy, historical war, siege, tactical simulation.
- Use carefully / avoid: atmosphere보다 fast modern scanning이 더 중요하면 피한다.
- Request UI rationale hints: command fantasy가 중심일 때 선택한다. tradeoff는 heavier visuals.

### Modular Dashboard Minimalism

- Definition: web dashboard와 simulation data surface를 결합한 game management UI.
- Visual cues: bento grid, chart, table, sidebar, detail panel, low decoration.
- Best fit: Sports management, tycoon, strategy economy, simulation admin screen.
- Use carefully / avoid: core game loop가 action 또는 emotion-led이면 피한다.
- Request UI rationale hints: data가 decision을 이끌 때 선택한다. tradeoff는 낮은 cinematic atmosphere.

### Skeuomorphic Skinned MMORPG

- Definition: themed skill slot, minimap, party state, quest tracker가 있는 dense RPG/MMO edge UI.
- Visual cues: gold/rune frame, edge-packed control, multi-tier skill pad, ornate quick slot.
- Best fit: Hardcore mobile MMORPG, action RPG, fantasy combat.
- Use carefully / avoid: combat view를 가리거나 tap target을 줄이지 않는다.
- Request UI rationale hints: player가 많은 persistent combat control을 기대할 때 선택한다. tradeoff는 clutter.

### Skeuomorphic Diegetic Hearth

- Definition: screen을 physical tabletop처럼 느끼게 하는 board/card game UI.
- Visual cues: wood/stone top-down surface, floating card/token, dice box, board object as menu control.
- Best fit: Digital board game, CCG, Hearthstone-like battler, tabletop adaptation.
- Use carefully / avoid: compact competitive clarity가 tabletop feel보다 중요하면 피한다.
- Request UI rationale hints: physical table presence가 재미의 일부일 때 선택한다. tradeoff는 heavy scene composition.

### Geometry Primitive Minimalism

- Definition: primitive shape, flat plane, minimal color로 game UI와 object를 통합한다.
- Visual cues: circles/squares/triangles, thin grid, monochrome base, one accent color, object/UI shape consistency.
- Best fit: Minimal arcade, 2048-like puzzle, hyper-casual, abstract action.
- Use carefully / avoid: narrative 또는 character-heavy game에는 피한다.
- Request UI rationale hints: rule clarity가 theme보다 중요할 때 선택한다. tradeoff는 낮은 atmosphere.

### Flat Cartoonish / Vector Playful

- Definition: cartoon simplicity로 entry barrier를 낮추는 friendly vector UI.
- Visual cues: bold stroke 또는 no stroke, flat color, rounded toy-like component, chunky type.
- Best fit: Party game, casual puzzle, family game, hidden-object, social game.
- Use carefully / avoid: tension, realism, premium seriousness가 필요하면 피한다.
- Request UI rationale hints: approachability와 instant charm이 중요할 때 선택한다. tradeoff는 depth 감소.

### Low-Poly Cozy Naturalism

- Definition: cozy, idle, healing game을 위한 warm low-poly/minimal 3D UI.
- Visual cues: low-poly object, pastel matte color, miniature lighting, rounded sans type, natural ambience.
- Best fit: Cozy idle, tycoon, pet/cat game, garden/town builder.
- Use carefully / avoid: high-precision competitive 또는 tactical surface에는 피한다.
- Request UI rationale hints: relaxation과 collection reward가 중요할 때 선택한다. tradeoff는 낮은 information density.

### Monochrome Silhouette

- Definition: silhouette와 backlight로 movement와 timing에 집중하는 artistic high-contrast UI.
- Visual cues: black silhouette, bright background, minimal text/number, shadow-theater composition.
- Best fit: Atmospheric platformer, minimal action, timing puzzle, art game.
- Use carefully / avoid: dense inventory, RPG stat, color-coded system에는 피한다.
- Request UI rationale hints: motion readability와 mood가 중요할 때 선택한다. tradeoff는 제한된 UI vocabulary.
