# PyWRKGame - Полная документация API

## Обзор

PyWRKGame - это профессиональный игровой движок для Python, специально оптимизированный для создания высокопроизводительных игр. Библиотека предоставляет полный набор инструментов для разработки игр от простых 2D проектов до сложных 3D приложений с поддержкой ray tracing, VR/AR, Web3 и многого другого.

**Версия:** 2.1.0  
**Лицензия:** MIT  
**Поддерживаемые платформы:** Windows, macOS, Linux, WebGL, игровые консоли  

---

## Основные модули

### 🎮 Core (Ядро)

#### Engine
Основной класс движка для управления игровым циклом.

```python
from pywrkgame import Engine, GameConfig

class Engine:
    def __init__(self, config: GameConfig)
    def init(self) -> bool
    def run(self, scene: Scene) -> None
    def shutdown(self) -> None
    def register_scene(self, name: str, scene: Scene) -> None
    def switch_scene(self, name: str) -> None
```

**Пример использования:**
```python
config = GameConfig(width=1280, height=720, title="My Game")
engine = Engine(config)
engine.init()
engine.run(my_scene)
```

#### GameConfig
Конфигурация игры с настройками окна, рендеринга и отладки.

```python
class GameConfig:
    def __init__(self):
        # Настройки окна
        self.window_width: int = 800
        self.window_height: int = 600
        self.window_title: str = "PyWRKGame"
        self.fullscreen: bool = False
        self.vsync: bool = True
        self.resizable: bool = True
        
        # Настройки рендеринга
        self.target_fps: int = 60
        self.max_frame_time: float = 1.0 / 30.0
        
        # Настройки отладки
        self.debug_mode: bool = False
        self.show_fps: bool = False
```

#### Scene
Базовый класс для игровых сцен с системой компонентов.

```python
class Scene:
    def on_enter(self) -> None
    def on_exit(self) -> None
    def update(self, dt: float) -> None
    def render(self, renderer: Renderer) -> None
    def handle_event(self, event: Event) -> None
    
    # Управление GameObject
    def add_game_object(self, obj: GameObject) -> None
    def remove_game_object(self, obj: GameObject) -> None
    def find_game_object(self, name: str) -> Optional[GameObject]
```

---

### 🎨 Graphics (Графика)

#### Renderer
Основная система рендеринга с поддержкой различных режимов.

```python
class Renderer:
    def clear(self, color: Color = Colors.BLACK) -> None
    def draw_sprite(self, texture: Texture, position: Vec2, size: Vec2) -> None
    def draw_text(self, text: str, position: Vec2, font: Font, color: Color) -> None
    def draw_rect(self, rect: Rect, color: Color, filled: bool = True) -> None
    def draw_circle(self, center: Vec2, radius: float, color: Color) -> None
    def draw_line(self, start: Vec2, end: Vec2, color: Color, width: float = 1.0) -> None
    
    # 3D рендеринг
    def draw_mesh(self, mesh: Mesh, material: Material, transform: Transform) -> None
    def set_camera(self, camera: Camera) -> None
    def set_lighting(self, lights: List[Light]) -> None
```

#### Ray Tracing (RTX/RDNA2 поддержка)
Первая Python библиотека с поддержкой аппаратного ray tracing!

```python
from pywrkgame.graphics.raytracing import RayTracingRenderer, RTMaterial, RTLight

class RayTracingRenderer:
    def __init__(self, device_type: str = "auto")  # "rtx", "rdna2", "cpu"
    def enable_ray_tracing(self) -> bool
    def create_rt_material(self, material_type: RTMaterialType) -> RTMaterial
    def add_rt_light(self, light: RTLight) -> None
    def render_with_rt(self, scene: Scene, camera: Camera) -> None
    
    # Продвинутые возможности
    def enable_global_illumination(self, enabled: bool) -> None
    def set_rt_quality(self, quality: RTQuality) -> None  # LOW, MEDIUM, HIGH, ULTRA
    def enable_denoising(self, enabled: bool) -> None
```

---

### 🔊 Audio (Аудио)

#### AudioEngine
3D пространственное аудио с продвинутыми эффектами.

```python
from pywrkgame.audio import AudioEngine, Sound, Music

class AudioEngine:
    def __init__(self, sample_rate: int = 44100, channels: int = 2)
    def load_sound(self, filepath: str) -> Sound
    def load_music(self, filepath: str) -> Music
    def play_sound(self, sound: Sound, volume: float = 1.0) -> AudioSource
    def play_music(self, music: Music, loop: bool = True) -> None
    
    # 3D аудио
    def set_listener_position(self, position: Vec3) -> None
    def play_3d_sound(self, sound: Sound, position: Vec3) -> AudioSource3D
```

---

### 🎯 Physics (Физика)

#### PhysicsEngine
Интеграция с PyBullet и Pymunk для реалистичной физики.

```python
from pywrkgame.physics import PhysicsEngine, RigidBody

class PhysicsEngine:
    def __init__(self, gravity: Vec3 = Vec3(0, -9.81, 0))
    def step(self, dt: float) -> None
    def add_rigid_body(self, body: RigidBody) -> None
    def raycast(self, start: Vec3, end: Vec3) -> RaycastResult

class RigidBody:
    def __init__(self, shape: CollisionShape, mass: float = 1.0)
    def apply_force(self, force: Vec3, point: Vec3 = None) -> None
    def apply_impulse(self, impulse: Vec3, point: Vec3 = None) -> None
```

---

### 🎮 Input (Ввод)

#### InputSystem
Универсальная система ввода для всех платформ.

```python
from pywrkgame.input import Keyboard, Mouse, Gamepad

class Keyboard:
    @staticmethod
    def is_key_pressed(key: KeyCode) -> bool
    def is_key_just_pressed(key: KeyCode) -> bool

class Mouse:
    @staticmethod
    def get_position() -> Vec2
    def is_button_pressed(button: MouseButton) -> bool

class Gamepad:
    def __init__(self, player_index: int = 0)
    def is_button_pressed(self, button: GamepadButton) -> bool
    def get_stick_position(self, stick: GamepadStick) -> Vec2
```

---

### 🌐 Platform Support (Поддержка платформ)

#### WebGL Platform
Первая Python библиотека с полной поддержкой WebGL!

```python
from pywrkgame.webgl import WebGLRenderer, WebGLPlatform
from pywrkgame.platforms import PlatformDetector, Platform

platform = PlatformDetector.detect_platform()
if platform == Platform.WEB_BROWSER:
    renderer = WebGLRenderer()
```

#### Console Support
Поддержка игровых консолей (первая в Python!).

```python
from pywrkgame.console import ConsoleDetector, ConsoleType

console_type = ConsoleDetector.detect_console()
if console_type == ConsoleType.PLAYSTATION_5:
    renderer = ConsoleRenderer(console_type)
```

---

### 🤖 AI Systems (ИИ системы)

#### AI Integration
Интеграция с современными ИИ технологиями.

```python
from pywrkgame.ai import GPTIntegration, ComputerVision, MLFeatures

class GPTIntegration:
    def __init__(self, api_key: str)
    def generate_dialogue(self, context: str, character: str) -> str
    def generate_quest(self, player_level: int, world_state: dict) -> Quest

class ComputerVision:
    def detect_objects(self, image: np.ndarray) -> List[DetectedObject]
    def track_motion(self, video_frames: List[np.ndarray]) -> MotionData
```

---

### 🥽 VR/AR Support

#### VR Integration
Поддержка VR/AR с OpenXR.

```python
from pywrkgame.vr import VRSystem, ARSystem

class VRSystem:
    def initialize(self) -> bool
    def get_hmd_pose(self) -> Transform
    def get_controller_pose(self, controller_id: int) -> Transform
    def submit_frame(self, eye: VREye, texture: Texture) -> None

class ARSystem:
    def start_ar_session(self) -> bool
    def get_camera_frame(self) -> CameraFrame
    def detect_planes(self) -> List[ARPlane]
```

---

### 🌐 Web3 Integration

#### Blockchain и NFT поддержка
Интеграция с блокчейн технологиями.

```python
from pywrkgame.web3 import SmartContracts, NFTAssets, CryptoPayments

class SmartContracts:
    def connect_wallet(self, wallet_type: WalletType) -> Wallet
    def deploy_contract(self, contract_code: str) -> Contract

class NFTAssets:
    def mint_nft(self, metadata: NFTMetadata) -> NFT
    def transfer_nft(self, nft: NFT, to_address: str) -> Transaction
```

---

## Быстрый старт

### Простейший пример

```python
from pywrkgame import quick_start, Scene, Colors

class MyGame(Scene):
    def update(self, dt):
        pass
    
    def render(self, renderer):
        renderer.clear(Colors.BLUE)
        renderer.draw_text("Hello PyWRKGame!", (100, 100))

# Запуск одной строчкой!
quick_start(MyGame, title="My First Game")
```

### Продвинутый пример с Ray Tracing

```python
from pywrkgame import Engine, GameConfig, Scene
from pywrkgame.graphics.raytracing import RayTracingRenderer

class RTGame(Scene):
    def __init__(self):
        super().__init__()
        self.rt_renderer = RayTracingRenderer("rtx")
        
    def render(self, renderer):
        self.rt_renderer.render_with_rt(self, self.camera)

config = GameConfig(width=1920, height=1080, title="RTX Demo")
engine = Engine(config)
engine.run(RTGame())
```

---

## Системные требования

### Минимальные требования
- **Python:** 3.8+
- **ОС:** Windows 10, macOS 10.14, Ubuntu 18.04
- **Память:** 4 GB RAM
- **Видеокарта:** OpenGL 3.3 / DirectX 11

### Рекомендуемые требования
- **Python:** 3.11+
- **ОС:** Windows 11, macOS 12+, Ubuntu 22.04
- **Память:** 16 GB RAM
- **Видеокарта:** RTX 3060 / RX 6600 XT (для ray tracing)

---

## Установка и настройка

```bash
# Базовая установка
pip install pywrkgame

# С поддержкой ray tracing
pip install pywrkgame[raytracing]

# Полная установка со всеми возможностями
pip install pywrkgame[full]
```

---

## Поддержка и сообщество

- **GitHub:** https://github.com/surgil-gh/pywrkgame
- **Документация:** https://pywrkgame.readthedocs.io(в будущем)
- **Discord:** https://discord.gg/pywrkgame(в будущем)
- **Форум:** https://forum.pywrkgame.com(в будущем)

---

*PyWRKGame - Создавайте игры будущего уже сегодня!* 🚀