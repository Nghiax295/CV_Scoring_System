# UI Rules - CVScoringSystem

## 🎨 Màu Sắc (Color Scheme)

### Primary Colors (Màu Chính)
- **status Indigo**: `blue-600` (#2563eb) - Màu chủ đạo
- **status Hovers**: `blue-500` (#3b82f6)
- **status Lighter**: `blue-50` (#eff6ff), `blue-100` (#dbeafe)
- **status Borders**: `border-blue-200`, `border-blue-600`

### Success Colors (Màu Thành Công)
- **#Green Primary**: `green-500` (#22c55e)
- **#Green Hover**: `green-600` (#16a34a)
- **#Green Lighter**: `green-50`, `green-100`
- **#Green Text**: `text-green-600`

### Error/Danger Colors (Màu Lỗi/Nguy Hiểm)
- **#Red Primary**: `red-500` (#ef4444)
- **#Red Hover**: `red-600` (#dc2626)
- **#Red Lighter**: `red-50`, `red-100`
- **#Red Text**: `text-red-600`

### Warning Colors (Màu Cảnh Báo)
- **#Yellow Primary**: `yellow-500` (#eab308)
- **#Yellow Hover**: `yellow-600` (#ca8a04)
- **#Yellow Lighter**: `yellow-50`
- **#Yellow Text**: `text-yellow-600`

### Background Colors
- **#White**: `bg-white` (#ffffff) - main background
- **#Backdrop**: `bg-black/50`, `bg-slate-50` - modal overlays
- **#Status transparencies**: `bg-white/70`, `bg-blue-50`
- **#Grid Transparencies**: `bg-slate/50`, `via-white/30`, `to-indigo-600`

### Text Colors
- **#Linear Gradient Backgrounds**:
  - Blue gradient: `bg-linear-to-br from-sky-400 via-blue-500 to-indigo-600`
  - Light gradient: `bg-linear-to-br from-blue-50 to-indigo-100`
  - Pattern: `bg-repeat bg-[length:40px_40px]`

### Border Colors
- **#Pattern**: `border border-slate-200`
- **#Light**: `border-blue-100`
- **#Status**: `border-blue-500`

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

## 🚫 Cấm Tuyệt Đối

### ❌ KHÔNG Sử Dụng
1. **Box Shadow**: Tuyệt đối KHÔNG dùng `shadow-*`
   - Thay thế: `border border-slate-200`

2. **Gradient Background Nhiều**: Hạn chế tối đa
   - Chỉ dùng cho hero section hoặc highlight
   - Ưu tiên solid colors

3. **Glassmorphism/Blur**: Hạn chế
   - KHÔNG dùng `backdrop-blur-*` trừ modal overlay

4. **Emoji Icons**: Tuyệt đối KHÔNG
   - Thay thế: Lucide Icons, Font Awesome

5. **Màu Xanh-Tím Mặc Định AI**: Hạn chế
   - Đã chọn blue-600 làm primary, tuân thủ nghiêm ngặt

6. **Border Radius Quá Đà**: 
   - KHÔNG rounded-full cho box lớn
   - Tuân thủ quy tắc cha > con

7. **Animation Lố Lạc**:
   - Animation phải mượt, chuyên nghiệp
   - Transition: `transition-all duration-200 ease-in-out`

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

### Transition Rules
- **Standard**: `transition-all duration-200 ease-in-out`
- **Fast**: `transition-all duration-150`
- **Slow**: `transition-all duration-300`

### Hover Effects
- **Button**: Đổi background color (không dùng shadow)
- **Card**: `border-blue-500` + slight scale
- **Link**: `text-blue-600` underline

### Animation Principles
- Mượt mà, không giật lag
- Đồng bộ trong toàn bộ hệ thống
- Không quá lố, chuyên nghiệp

## 🧩 Components

### Button
```html
<!-- Primary Button -->
<button class="px-6 py-3 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-500 transition-all duration-200">
    Text
</button>

<!-- Secondary Button -->
<button class="px-6 py-3 border border-blue-600 text-blue-600 rounded-lg font-medium hover:bg-blue-50 transition-all duration-200">
    Text
</button>

<!-- Success Button -->
<button class="px-6 py-3 bg-green-500 text-white rounded-lg font-medium hover:bg-green-600 transition-all duration-200">
    Text
</button>
```

### Card
```html
<div class="p-6 bg-white border border-slate-200 rounded-xl">
    <!-- Content -->
</div>
```

### Input
```html
<input type="text" class="px-4 py-2 border border-slate-200 rounded-md focus:border-blue-600 focus:outline-none transition-all duration-200">
```

### Badge
```html
<span class="px-3 py-1 bg-blue-100 text-blue-600 text-sm rounded-lg">
    Status
</span>
```

### Table
```html
<table class="w-full border border-slate-200">
    <thead class="bg-slate-50">
        <tr>
            <th class="px-6 py-3 text-left text-sm font-semibold">Header</th>
        </tr>
    </thead>
    <tbody>
        <tr class="border-t border-slate-200 hover:bg-slate-50 transition-all duration-200">
            <td class="px-6 py-4">Data</td>
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

### Accessibility
- Contrast ratio tối thiểu: 4.5:1
- Focus states rõ ràng: `focus:ring-2 focus:ring-blue-600`
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
