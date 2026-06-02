# 🪟 透明物理幕布 · Transparent Physical Curtain

> *屏幕里挂一块隐形的布 — 用手指捏合抓住它，掀开看背后。*

**光学伪装 × 布料物理 × 手势交互** — 基于 p5.js + MediaPipe Hands 的单文件 HTML 实时交互体验。

<p align="center">
  <img src="screenshots/curtain-preview.png" alt="透明物理幕布预览" width="720" />
</p>

---

## 功能列表

| 类别 | 功能 | 状态 |
|------|------|:---:|
| 🎭 **光学伪装** | 三层渲染：底层全屏摄像头、中层隐藏媒体、顶层 clip 伪装 | ✅ |
| 🧵 **布料物理** | Verlet 积分 38×35 网格，12 次约束迭代，Perlin 噪声微风 | ✅ |
| ✨ **质感渲染** | Quad 面积比褶皱阴影/高光 + 液态光泽边缘描边 | ✅ |
| ✋ **手势识别** | MediaPipe Hands 21 点关键点，双手同时操作 | ✅ |
| 🤏 **捏合抓取** | pinch 迟滞检测（按下 0.06 / 松开 0.09），帧间 200px 追踪 | ✅ |
| 🚀 **甩起落下** | 松手垂直速度 → fling-up 飞起挂顶 / fling-down 缓慢落下 | ✅ |
| 🔒 **挂顶锁定** | fling-up 后布料锁在顶部，捏合任意位置下拉解锁 | ✅ |
| 🖱️ **鼠标/触摸** | 完整 fallback，无摄像头时仍可体验 | ✅ |
| 📱 **移动端** | `touch-action: none`，禁止滚动+双指缩放，自适应布局 | ✅ |
| 📤 **媒体上传** | 图片/视频上传，自适应布料宽高比（0.85×0.55 屏幕区域）| ✅ |
| 📊 **揭示百分比** | 左下角实时 Reveal% 进度条 | ✅ |
| ⌨️ **快捷键** | `H` 手部标记 / `D` 调试辅助线 | ✅ |

---

## 技术栈

```
┌─────────────────────────────────────────────┐
│              index.html (1135 行)            │
├─────────────────────────────────────────────┤
│  p5.js 1.11.3       渲染引擎 / 画布 / 数学   │
│  MediaPipe Hands     21 点手部关键点检测      │
│  Canvas 2D API       三层 clip 复合渲染      │
│  Verlet Integration  布料物理模拟             │
│  Perlin Noise        微风呼吸感               │
│  Flask (可选)        本地开发服务器           │
└─────────────────────────────────────────────┘
```

| 维度 | 详情 |
|------|------|
| 语言 | HTML5 + JavaScript (ES6+) |
| 外部依赖 | p5.js CDN, @mediapipe/hands CDN |
| 构建 | 零构建 — 浏览器直接打开 |
| 兼容性 | Chrome / Edge / Safari (WebAssembly + WebRTC) |
| 代码量 | 单文件 ~1135 行，无框架 |

---

## 使用方法

### 快速启动

```bash
# 方式 1：Flask（推荐 — 提供 localhost，摄像头 API 需要安全上下文）
cd D:\_project\c\HelloWorld
python app.py
# 浏览器打开 http://127.0.0.1:5000

# 方式 2：Python HTTP Server
python -m http.server 8000
# 浏览器打开 http://localhost:8000/templates/index.html

# 方式 3：VS Code Live Server
# 右键 templates/index.html → Open with Live Server
```

### 操作流程

1. 点击「**开始**」→ 允许摄像头权限
2. 点击右下角 🖼 → 上传一张图片或视频
3. **拇指食指捏合** (pinch)，靠近幕布
4. 捏合状态下拖动 → 幕布被揭开，背后画面浮现
5. 松手 → 布料恢复自然悬垂

---

## 手势说明

| 手势 | 操作 | 效果 |
|------|------|------|
| 🤏 **捏合** (Pinch) | 拇指 + 食指捏合 | 抓取幕布 |
| ✋ **拖动** | 捏合状态下移动手 | 布料跟随手部变形 |
| ⬆️ **向上甩** | 捏合松开时手向上挥 (vy < -15) | 幕布飞起吸顶 → **锁定挂顶** |
| ⬇️ **向下拉** | 挂顶状态下任意位置捏合下拉 | 解锁 → 幕布自然落下 |
| 🔓 **任意解锁** | 挂顶状态鼠标/触摸任意位置 | 立即解锁下落 |

### 捏合阈值

```
捏合按下:  拇指-食指归一化距离 < 0.06
捏合松开:  距离 > 0.09 (迟滞防抖)
抓取半径:  150px (画布坐标)
手部追踪:  帧间 200px 半径匹配
```

---

## 鼠标操作说明

| 操作 | 效果 |
|------|------|
| 🖱️ **点击拖拽** | 抓取最近网格点，布料跟随变形 |
| ⬆️ **快速上甩松开** | fling-up → 飞起挂顶 |
| ⬇️ **快速下拉松开** | fling-down → 缓慢回落 |
| 🖱️ **任意位置点击** (挂顶时) | 解锁下落 |

---

## 移动端支持

| 特性 | 实现 |
|------|------|
| 禁止滚动 | `touch-action: none` |
| 禁止双指缩放 | `user-scalable=no` |
| 视口适配 | `viewport-fit=cover` |
| 自拍摄像头 | `facingMode: 'user'`，x 轴镜像 |
| 后置摄像头 | 点击 🔄 翻转切换 |
| UI 隐藏 | 点击 👁 进入沉浸模式 |

---

## 键盘快捷键

| 按键 | 功能 | 默认 |
|------|------|:---:|
| `H` | 切换手部关键点标记 | 关 |
| `D` | 切换布料调试辅助线 | 关 |

---

## 性能参数

| 参数 | 值 | 说明 |
|------|----|------|
| 网格密度 | 38×35 (1330 点) | Verlet 积分 |
| 约束迭代 | 12 次/帧 | stiffness 0.4 |
| MediaPipe 帧率 | ~15 fps | 节流 + 忙锁 |
| 目标帧率 | 60 fps | p5.js 渲染 |
| 内存策略 | 零 per-frame 对象创建 | 复用缓存 |
| 文件大小 | ~50 KB (gzip 前) | 单文件 |

---

## GitHub Pages 部署

```bash
# 1. 将 index.html 放到仓库根目录
cp templates/index.html index.html

# 2. 推送到 GitHub
git add index.html
git commit -m "Deploy: Transparent Physical Curtain"
git push origin feature/transparent-cloth

# 3. 在仓库 Settings → Pages 中启用：
#    Source: Deploy from a branch
#    Branch: feature/transparent-cloth  / (root)

# 4. 访问 https://<username>.github.io/<repo>/
```

> ⚠️ GitHub Pages 使用 HTTPS，满足 `getUserMedia()` 安全上下文要求。

---

## 项目截图

> *请将截图放入 `screenshots/` 目录后取消注释*

```html
<!-- 截图占位 -->
<!--
| 场景 | 预览 |
|------|------|
| 初始状态 — 布料下垂 | ![初始状态](screenshots/idle.png) |
| 手势捏合抓取 | ![手势抓取](screenshots/pinch-grab.png) |
| 揭开后 — 背后图片露出 | ![揭开效果](screenshots/revealed.png) |
| 挂顶锁定状态 | ![挂顶锁定](screenshots/pinned.png) |
| 手机端体验 | ![移动端](screenshots/mobile.png) |
-->
```

---

## 文件结构

```
HelloWorld/
├── templates/
│   └── index.html      ← ★ 主文件（1135 行，单文件完整应用）
├── app.py              ← Flask 开发服务器（可选）
├── README.md           ← 本文件
└── screenshots/        ← 截图目录（待添加）
```

---

## 物理参数

| 常量 | 值 | 说明 |
|------|----|------|
| `COLS × ROWS` | 38 × 35 | 网格分辨率 |
| `FRICTION` | 0.94 | 空气阻力 |
| `GRAVITY` | 0.08 | 重力加速度 |
| `STIFFNESS` | 0.4 | 约束刚度（偏软，避免锁死）|
| `TOP_ROW_STIFFNESS_X` | 0.35 | 顶行横向恢复力 |
| `TOP_ROW_STIFFNESS_Y` | 0.18 | 顶行纵向恢复力（软，允许下拉）|
| `FLING_UP_RESTORE` | 0.02 | 飞起恢复力（快速吸顶）|
| `FLING_DOWN_RESTORE` | 0.0011 | 落下恢复力（缓慢下垂）|

---

## 后续规划

- [ ] 多语言支持 (i18n)
- [ ] 录制/回放手势序列
- [ ] WebSocket 多人协作（两人同时掀同一块布）
- [ ] 自定义布料纹理材质
- [ ] 3D 布料效果 (WebGL / Three.js)
- [ ] PWA 离线支持
- [ ] Electron 桌面应用封装
- [ ] 色盲友好模式

---

## 致谢

- [p5.js](https://p5js.org/) — 创意编程库
- [MediaPipe Hands](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker) — Google 手部关键点检测
- Verlet 积分论文: [Advanced Character Physics](https://www.cs.cmu.edu/afs/cs/academic/class/15462-s13/www/lec_slides/Jakobsen.pdf)

---

## License

MIT License — 详见 [LICENSE](LICENSE) 文件。
