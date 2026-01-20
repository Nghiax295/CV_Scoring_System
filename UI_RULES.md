# UI Rules - CVScoringSystem (Cyan Dark Theme)

## 🎨 Màu Sắc (Color Scheme)

### Primary Colors (Màu Chính - Cyan/Teal Theme)

- **Cyan Primary**: `cyan-500` (#06b6d4) - Màu chủ đạo
- **Cyan Bright**: `cyan-400` (#22d3ee) - Highlights
- **Cyan Hover**: `cyan-600` (#0891b2)
- **Cyan Glow**: `cyan-500/50` - Cho shadow effects
- **Cyan Light**: `cyan-300` (#67e8f9)
- **Cyan Lighter**: `cyan-50` (#ecfeff), `cyan-100` (#cffafe)

### Dark Theme Background

- **Primary BG**: `bg-slate-900` (#0f172a) - Main dark background
- **Secondary BG**: `bg-slate-800` (#1e293b) - Card/section background
- **Tertiary BG**: `bg-slate-700` (#334155) - Hover states
- **Navy Dark**: `bg-[#0a1628]` - Deepest background
- **Gradient BG**: `bg-gradient-to-br from-slate-900 via-slate-800 to-cyan-900/20`

### Teal/Turquoise Accent

- **Teal Primary**: `teal-500` (#14b8a6)
- **Teal Bright**: `teal-400` (#2dd4bf)
- **Teal Dark**: `teal-600` (#0d9488)
- **Teal Glow**: `teal-400/30`

### Text Colors (Dark Theme)

- **Primary Text**: `text-white` (#ffffff)
- **Secondary Text**: `text-slate-300` (#cbd5e1)
- **Muted Text**: `text-slate-400` (#94a3b8)
- **Cyan Text**: `text-cyan-400`, `text-cyan-300`
- **Heading Gradient**: `bg-gradient-to-r from-cyan-400 to-teal-400 bg-clip-text text-transparent`

### Success Colors

- **Emerald Primary**: `emerald-500` (#10b981)
- **Emerald Glow**: `emerald-400/30`

### Error/Danger Colors

- **Rose Primary**: `rose-500` (#f43f5e)
- **Rose Glow**: `rose-400/30`

### Warning Colors

- **Amber Primary**: `amber-500` (#f59e0b)
- **Amber Glow**: `amber-400/30`

### Glassmorphism & Effects (CHO PHÉP)

- **Glass Background**: `bg-white/5`, `bg-slate-800/50`
- **Backdrop Blur**: `backdrop-blur-sm`, `backdrop-blur-md`, `backdrop-blur-lg`
- **Border Glow**: `border border-cyan-500/50` + `shadow-[0_0_15px_rgba(6,182,212,0.3)]`
- **Neon Glow**: `shadow-[0_0_20px_rgba(6,182,212,0.5)]`

### Gradient Backgrounds (CHO PHÉP RỘNG RÃI)

- **Cyan Gradient**: `bg-gradient-to-br from-cyan-400 via-cyan-500 to-teal-600`
- **Button Gradient**: `bg-gradient-to-r from-cyan-500 to-teal-500`
- **Dark Gradient**: `bg-gradient-to-br from-slate-900 via-slate-800 to-cyan-900/30`
- **Glow Gradient**: `bg-gradient-to-r from-cyan-500/20 to-teal-500/20`

### Border & Glow Effects

- **Default Border**: `border border-slate-700`
- **Cyan Border**: `border border-cyan-500/50`
- **Glow Border**: `border border-cyan-500 shadow-[0_0_15px_rgba(6,182,212,0.3)]`
- **Active Glow**: `border-cyan-400 shadow-[0_0_25px_rgba(34,211,238,0.5)]`

## 📏 Spacing (Khoảng Cách)

### Primary Spacing Scale

- `space-8`: `8px` (0.5rem) - Minimal spacing
- `space-12`: `12px` (0.75rem) - Tight spacing
- `space-16`: `16px` (1rem) - Base spacing
- `space-24`: `24px` (1.5rem) - Medium spacing
- `space-32`: `32px` (2rem) - Large spacing
- `space-48`: `48px` (3rem) - Section spacing

### Component Spacing

- **Input padding**: `px-4 py-2` (16px horizontal, 8px vertical)
- **Button padding**: `px-5 py-2.5` hoặc `px-6 py-3`
- **Card padding**: `p-6` (24px)
- **Section padding**: `py-12` (48px vertical)

## 🔠 Typography (Kiểu Chữ)

### Font Family

- **#Primary Font**: `"Be Vietnam Pro"` (sans-serif)
  - Body text: `400` (regular), `500` (medium)
  - Important text: `600` (semibold)
- **#Heading Font**: `"Montserrat Alternates"` (sans-serif)
  - Font weight: `600` (semibold), `700` (bold)

### Font Sizes

- **Heading 1**: `text-4xl` (36px) hoặc `text-5xl` (48px)
- **Heading 2**: `text-3xl` (30px)
- **Heading 3**: `text-2xl` (24px)
- **Heading 4**: `text-xl` (20px)
- **Body Large**: `text-lg` (18px)
- **Body**: `text-base` (16px)
- **Body Small**: `text-sm` (14px)
- **Caption**: `text-xs` (12px)

### Font Config

```python
FONT_CONFIG = {
    'heading': 'Montserrat Alternates, sans-serif',
    'body': 'Be Vietnam Pro, sans-serif'
}
```

## 🔲 Border Radius (Bo Góc)

### Component Radius

- **Button**: `rounded-lg` (12px)
- **Card Large**: `rounded-xl` (16px)
- **Card Medium**: `rounded-lg` (12px)
- **Input**: `rounded-md` (8px)
- **Badge/Tag**: `rounded-full` hoặc `rounded-lg`
- **Modal**: `rounded-2xl` (20px)

### Rules

- Container cha LUÔN có radius lớn hơn hoặc bằng con
- Tránh tất cả element cùng radius

## ✨ Hiệu Ứng Hiện Đại (Modern Effects)

### ✅ CHO PHÉP Sử Dụng (Dark Theme Design)

1. **Glow Effects & Neon Borders**: Khuyến khích
   - `shadow-[0_0_15px_rgba(6,182,212,0.3)]` - Cyan glow
   - `shadow-[0_0_20px_rgba(6,182,212,0.5)]` - Strong glow
   - Dùng cho buttons, cards, borders

2. **Glassmorphism**: Khuyến khích mạnh mẽ
   - `backdrop-blur-md`, `backdrop-blur-lg`
   - `bg-white/5`, `bg-slate-800/50`
   - Dùng cho cards, modals, panels

3. **Gradient Backgrounds**: Sử dụng tự do
   - Cyan gradients cho buttons: `bg-gradient-to-r from-cyan-500 to-teal-500`
   - Dark gradients cho backgrounds
   - Animated gradients cho hero sections

4. **3D Effects & Perspective**: Cho phép
   - `transform-style: preserve-3d`
   - Perspective effects như trong ảnh reference
   - Subtle 3D transforms

5. **Border Glow & Neon**: Khuyến khích
   - `border-cyan-500 shadow-[0_0_15px_rgba(6,182,212,0.3)]`
   - Animated glow effects
   - Hover state glow intensify

### ⚠️ Hạn Chế Sử Dụng

1. **Emoji Icons**: Tuyệt đối KHÔNG
   - Thay thế: Lucide Icons, Font Awesome

2. **Border Radius Quá Đà**:
   - KHÔNG rounded-full cho box lớn
   - Tuân thủ quy tắc cha > con

3. **Animation Quá Nhiều**:
   - Animation phải mượt, có mục đích
   - Transition: `transition-all duration-300 ease-in-out`

## 🎭 Icons

### Icon Library

- **Lucide Icons** (priority)
- **Font Awesome** (fallback)

### Icon Sizes

- Small: `w-4 h-4` (16px)
- Medium: `w-5 h-5` (20px)
- Large: `w-6 h-6` (24px)
- Extra Large: `w-8 h-8` (32px)

### Icon Style

- Outline style ưu tiên
- Solid style cho filled states
- Color: kế thừa từ text color

## 🎬 Animation & Transitions

### Transition Rules (Dark Theme)

- **Standard**: `transition-all duration-300 ease-in-out`
- **Fast**: `transition-all duration-200`
- **Slow/Smooth**: `transition-all duration-500 ease-out`
- **Glow Animation**: `transition-shadow duration-300`

### Hover Effects (Dark Theme)

- **Button**: Glow intensify + color brighten
  ```css
  hover:shadow-[0_0_25px_rgba(34,211,238,0.6)] hover:bg-cyan-400
  ```
- **Card**: Cyan border glow + scale
  ```css
  hover:border-cyan-400 hover:shadow-[0_0_20px_rgba(6,182,212,0.4)] hover:scale-[1.02]
  ```
- **Link**: `text-cyan-400` with glow
  ```css
  hover:text-cyan-300 hover:drop-shadow-[0_0_8px_rgba(6,182,212,0.5)]
  ```

### Animation Principles

- Mượt mà, không giật lag
- Đồng bộ trong toàn bộ hệ thống
- Không quá lố, chuyên nghiệp

## 🧩 Components (Dark Theme với Glow Effects)

### Button

```html
<!-- Primary Cyan Button với Glow -->
<button
  class="px-6 py-3 bg-gradient-to-r from-cyan-500 to-teal-500 text-white rounded-lg font-medium 
         shadow-[0_0_15px_rgba(6,182,212,0.3)] hover:shadow-[0_0_25px_rgba(34,211,238,0.6)] 
         hover:from-cyan-400 hover:to-teal-400 transition-all duration-300"
>
  Login
</button>

<!-- Glassmorphism Button -->
<button
  class="px-6 py-3 bg-white/10 backdrop-blur-md border border-cyan-500/50 text-white rounded-lg 
         font-medium shadow-[0_0_10px_rgba(6,182,212,0.2)] hover:border-cyan-400 
         hover:shadow-[0_0_20px_rgba(6,182,212,0.4)] transition-all duration-300"
>
  Sign Up
</button>

<!-- Success Button -->
<button
  class="px-6 py-3 bg-emerald-500 text-white rounded-lg font-medium 
         shadow-[0_0_15px_rgba(16,185,129,0.3)] hover:bg-emerald-400 
         hover:shadow-[0_0_25px_rgba(16,185,129,0.5)] transition-all duration-300"
>
  Submit
</button>
```

### Card (Glassmorphism với Glow Border)

```html
<!-- Login Card Example (như trong video) -->
<div
  class="p-8 bg-slate-800/50 backdrop-blur-lg border border-cyan-500/50 
            rounded-2xl shadow-[0_0_20px_rgba(6,182,212,0.3)]
            hover:border-cyan-400 hover:shadow-[0_0_30px_rgba(6,182,212,0.5)]
            transition-all duration-300"
>
  <h2
    class="text-3xl font-bold bg-gradient-to-r from-cyan-400 to-teal-400 
             bg-clip-text text-transparent mb-6"
  >
    WELCOME BACK!
  </h2>
  <!-- Content -->
</div>

<!-- Simple Glassmorphism Card -->
<div
  class="p-6 bg-white/5 backdrop-blur-md border border-slate-700 rounded-xl
            hover:bg-white/10 transition-all duration-300"
>
  <!-- Content -->
</div>
```

### Input (Dark Theme)

```html
<div class="space-y-2">
  <label class="text-slate-300 text-sm font-medium">Username</label>
  <input
    type="text"
    class="w-full px-4 py-3 bg-slate-900/50 backdrop-blur-sm 
           border border-slate-700 rounded-lg text-white
           focus:border-cyan-500 focus:shadow-[0_0_15px_rgba(6,182,212,0.3)]
           focus:outline-none transition-all duration-300"
    placeholder="Enter username"
  />
</div>
```

### Badge (Cyan Theme)

```html
<!-- Primary Badge -->
<span
  class="px-3 py-1 bg-cyan-500/20 text-cyan-400 text-sm rounded-lg 
             border border-cyan-500/30 shadow-[0_0_8px_rgba(6,182,212,0.2)]"
>
  Active
</span>

<!-- Success Badge -->
<span
  class="px-3 py-1 bg-emerald-500/20 text-emerald-400 text-sm rounded-lg 
             border border-emerald-500/30"
>
  Completed
</span>
```

### Table (Dark Theme)

```html
<table class="w-full border border-slate-700 rounded-lg overflow-hidden">
  <thead class="bg-slate-800/70 backdrop-blur-sm">
    <tr>
      <th class="px-6 py-3 text-left text-sm font-semibold text-cyan-400">
        Name
      </th>
      <th class="px-6 py-3 text-left text-sm font-semibold text-cyan-400">
        Status
      </th>
    </tr>
  </thead>
  <tbody class="bg-slate-900/30">
    <tr
      class="border-t border-slate-700 hover:bg-slate-800/50 
               hover:shadow-[inset_0_0_10px_rgba(6,182,212,0.1)]
               transition-all duration-200"
    >
      <td class="px-6 py-4 text-slate-300">John Doe</td>
      <td class="px-6 py-4">
        <span
          class="px-2 py-1 bg-emerald-500/20 text-emerald-400 text-xs rounded"
        >
          Active
        </span>
      </td>
    </tr>
  </tbody>
</table>
```

## 📱 Responsive Design

### Breakpoints (Tailwind)

- `sm`: 640px
- `md`: 768px
- `lg`: 1024px
- `xl`: 1280px
- `2xl`: 1536px

### Mobile First

- Design cho mobile trước
- Progressive enhancement cho desktop
- Touch-friendly (min 44px tap targets)

## 🎯 Best Practices

### Layout

- Container max-width: `max-w-7xl mx-auto px-4`
- Grid gaps: `gap-4`, `gap-6`, `gap-8`
- Flexbox spacing: `space-x-*`, `space-y-*`

### Accessibility (Dark Theme)

- Contrast ratio tối thiểu: 4.5:1 (text trắng/cyan trên dark background)
- Focus states rõ ràng: `focus:ring-2 focus:ring-cyan-500 focus:shadow-[0_0_15px_rgba(6,182,212,0.3)]`
- Skip links cho keyboard navigation
- ARIA labels đầy đủ
- Color contrast: Cyan-400 (#22d3ee) trên slate-900 = 8.2:1 ✅

### Performance

- Lazy load images với placeholders
- Optimize glassmorphism (sử dụng backdrop-filter có chừng mực)
- Debounce animations
- Use CSS transforms thay vì position changes
- Limit glow effects đến 3-4 elements per view

---

## 🎨 Design Philosophy (Dark Cyan Theme)

1. **Consistency**: Tuân thủ color scheme và spacing
2. **Minimalism**: Chỉ dùng glow effects khi cần highlight
3. **Professional**: Dark theme với cyan accents tạo cảm giác hiện đại, chuyên nghiệp
4. **User-First**: Accessibility và UX luôn ưu tiên
5. **Scalable**: Components có thể tái sử dụng
6. **Modern**: Glassmorphism, glow effects, gradients cho UI hiện đại
7. **Cohesive**: Cyan color scheme xuyên suốt toàn bộ app

- Alt text cho images
- Semantic HTML

### Performance

- Lazy load images
- Minimize CSS bundle
- Optimize fonts loading

## 🔄 Update Rules

Khi cần thay đổi style:

1. Update file này TRƯỚC
2. Review toàn bộ UI cũ
3. Áp dụng đồng bộ cho toàn hệ thống
4. Test trên nhiều màn hình

---

**Version**: 1.0  
**Last Updated**: 20/01/2026  
**Project**: CVScoringSystem
