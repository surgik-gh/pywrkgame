# PyWRKGame - Справочник импортов

## Все возможные `from pywrkgame.* import *`

Этот файл содержит полный список всех модулей PyWRKGame, которые можно импортировать с помощью `from ... import *`.

---

## 🎮 Основные модули (Core)

### Ядро движка
```python
from pywrkgame import *                    # Основные классы: Engine, Scene, GameConfig, quick_start
from pywrkgame.core import *               # Все основные компоненты
from pywrkgame.core.game import *          # GameConfig, GameStats
from pywrkgame.core.scene import *         # Scene, GameObject, Transform, ComponentType
from pywrkgame.core.window import *        # Window, WindowConfig
from pywrkgame.core.event_system import *  # EventSystem, Event, EventType
from pywrkgame.core.resource_manager import *  # ResourceManager, Resource
from pywrkgame.core.assets import *        # AssetManager, assets (глобальный объект)
from pywrkgame.core.wrk_parser import *    # WRKParser
```

### Компоненты
```python
from pywrkgame.components import *          # Все компоненты
from pywrkgame.components.mesh_renderer import *  # MeshRenderer
```

---

## 🎨 Графика (Graphics)

### Основной рендеринг
```python
from pywrkgame.graphics import *            # Renderer, Camera, Material, Mesh
from pywrkgame.graphics.renderer import *   # Renderer, BlendMode, RenderState
from pywrkgame.graphics.simple_renderer import *  # SimpleRenderer
from pywrkgame.graphics.sprite_renderer import *  # SpriteRenderer
from pywrkgame.graphics.color import *      # Colors, Color
```

### Ray Tracing (RTX/RDNA2)
```python
from pywrkgame.graphics.raytracing import *           # Все RT компоненты
from pywrkgame.graphics.raytracing.rt_core import *   # RayTracingCore, RTSupport
from pywrkgame.graphics.raytracing.rt_renderer import *  # RayTracingRenderer
from pywrkgame.graphics.raytracing.rt_materials import *  # RTMaterial, RTMaterialType
from pywrkgame.graphics.raytracing.rt_lighting import *   # RTLight, RTLightType
from pywrkgame.graphics.raytracing.rt_shadows import *    # RTShadows
from pywrkgame.graphics.raytracing.rt_reflections import *  # RealtimeReflections
from pywrkgame.graphics.raytracing.rt_cupy_integration import *  # CuPyIntegration
from pywrkgame.graphics.raytracing.rt_gpu_acceleration import *  # GPUAcceleration
```

### Post-Processing
```python
from pywrkgame.graphics.postprocessing import *           # Все эффекты
from pywrkgame.graphics.postprocessing.post_processor import *  # PostProcessor
from pywrkgame.graphics.postprocessing.effects import *   # PostProcessEffect
from pywrkgame.graphics.postprocessing.bloom import *     # BloomEffect
from pywrkgame.graphics.postprocessing.dof import *       # DOFEffect
from pywrkgame.graphics.postprocessing.motion_blur import *  # MotionBlurEffect
from pywrkgame.graphics.postprocessing.ssr import *       # SSREffect
from pywrkgame.graphics.postprocessing.taa import *       # TAAEffect
from pywrkgame.graphics.postprocessing.tonemapping import *  # TonemappingEffect
from pywrkgame.graphics.postprocessing.volumetric import *   # VolumetricEffect
```

### Процедурная генерация
```python
from pywrkgame.graphics.procedural import *           # Все генераторы
from pywrkgame.graphics.procedural.noise import *     # NoiseGenerator, PerlinNoise
from pywrkgame.graphics.procedural.terrain import *   # TerrainGenerator
from pywrkgame.graphics.procedural.textures import *  # TextureGenerator
from pywrkgame.graphics.procedural.animation import * # AnimationGenerator
from pywrkgame.graphics.procedural.cellular import *  # CellularAutomata
from pywrkgame.graphics.procedural.lsystems import *  # LSystemGenerator
from pywrkgame.graphics.procedural.ml_generation import *  # MLGenerator
```

### Кинематографические эффекты
```python
from pywrkgame.graphics.cinematic_camera import *    # CinematicCamera
from pywrkgame.graphics.cinematic_lighting import *  # CinematicLighting
from pywrkgame.graphics.cinematic_materials import * # CinematicMaterials
from pywrkgame.graphics.cinematic_timeline import *  # CinematicTimeline
```

---

## 🎯 Физика (Physics)

```python
from pywrkgame.physics import *              # PhysicsEngine, RigidBody, CollisionShape
from pywrkgame.physics.rigidbody import *    # RigidBody, PhysicsBody
from pywrkgame.physics.softbody import *     # SoftBody, ClothSimulation
from pywrkgame.physics.fluids import *       # FluidSimulation, FluidEmitter
from pywrkgame.physics.destruction import *  # DestructionSystem, Fracture
```

---

## 🔊 Аудио (Audio)

```python
from pywrkgame.audio import *                # AudioEngine, Sound, Music, AudioSource
```

---

## 🎮 Ввод (Input)

```python
from pywrkgame.input import *                # Все системы ввода
from pywrkgame.input.keyboard import *       # Keyboard, KeyCode
from pywrkgame.input.mouse import *          # Mouse, MouseButton
from pywrkgame.input.gamepad import *        # Gamepad, GamepadButton, GamepadStick
```

---

## 🌐 Платформы (Platforms)

### Определение платформ
```python
from pywrkgame.platforms import *                    # Все платформы
from pywrkgame.platforms.platform_detector import * # PlatformDetector, Platform
from pywrkgame.platforms.desktop_platform import *  # DesktopPlatform
from pywrkgame.platforms.webgl_platform import *    # WebGLPlatform
from pywrkgame.platforms.console_platform import *  # ConsolePlatform
```

### WebGL поддержка
```python
from pywrkgame.webgl import *                    # Все WebGL компоненты
from pywrkgame.webgl.webgl_context import *     # WebGLContext
from pywrkgame.webgl.webgl_renderer import *    # WebGLRenderer
from pywrkgame.webgl.webgl_shader import *      # WebGLShader
from pywrkgame.webgl.webgl_buffer import *      # WebGLBuffer
from pywrkgame.webgl.webgl_texture import *     # WebGLTexture
from pywrkgame.webgl.webgl_utils import *       # WebGLUtils
from pywrkgame.webgl.browser_bridge import *    # BrowserBridge
from pywrkgame.webgl.pyodide_integration import *  # PyodideIntegration
```

### Консольная поддержка
```python
from pywrkgame.console import *                    # Все консольные компоненты
from pywrkgame.console.console_detector import *   # ConsoleDetector, ConsoleType
from pywrkgame.console.console_renderer import *   # ConsoleRenderer
from pywrkgame.console.console_input import *      # ConsoleInput, GamepadButton
from pywrkgame.console.playstation import *        # PlayStation5, PS5Features
from pywrkgame.console.xbox import *               # XboxSeriesX, XboxFeatures
from pywrkgame.console.nintendo_switch import *    # NintendoSwitch, SwitchFeatures
```

---

## 🤖 ИИ (AI)

```python
from pywrkgame.ai import *                    # Все ИИ компоненты
from pywrkgame.ai.gpt_integration import *    # GPTIntegration, GPTConfig
from pywrkgame.ai.computer_vision import *    # ComputerVision, ObjectDetection
from pywrkgame.ai.ml_features import *        # MLFeatures, BehaviorModel
```

---

## 🥽 VR/AR

```python
from pywrkgame.vr import *                    # Все VR/AR компоненты
from pywrkgame.vr.openxr_integration import * # OpenXRIntegration, VRSystem
from pywrkgame.vr.vr_ui import *              # VRUI, VRInteraction
from pywrkgame.vr.ar_tracking import *        # ARTracking, ARPlane
from pywrkgame.vr.mixed_reality import *      # MixedReality, MRFeatures
```

---

## 🌐 Web3

```python
from pywrkgame.web3 import *                      # Все Web3 компоненты
from pywrkgame.web3.smart_contracts import *      # SmartContracts, Contract
from pywrkgame.web3.nft_assets import *           # NFTAssets, NFT
from pywrkgame.web3.crypto_payments import *       # CryptoPayments, Wallet
from pywrkgame.web3.wallet_integration import *    # WalletIntegration
from pywrkgame.web3.ipfs_storage import *         # IPFSStorage
from pywrkgame.web3.decentralized_multiplayer import *  # DecentralizedMultiplayer
```

---

## 🚀 Оптимизация (Optimization)

```python
from pywrkgame.optimization import *              # Все оптимизации
from pywrkgame.optimization.cpu import *          # CPUOptimization
from pywrkgame.optimization.gpu_compute import *  # GPUCompute
from pywrkgame.optimization.memory import *       # MemoryOptimization
from pywrkgame.optimization.cross_platform import *  # CrossPlatformOptimization
```

---

## 🔬 Квантовые вычисления (Quantum)

```python
from pywrkgame.quantum import *              # Все квантовые компоненты
from pywrkgame.quantum.quantum_rng import *  # QuantumRNG
from pywrkgame.quantum.crypto import *       # QuantumCrypto
from pywrkgame.quantum.ml import *           # QuantumML
```

---

## 🌐 Мультиплеер (Multiplayer)

```python
from pywrkgame.multiplayer import *            # Все сетевые компоненты
from pywrkgame.multiplayer.networking import * # NetworkManager, Client, Server
from pywrkgame.multiplayer.distributed import * # DistributedSystem
from pywrkgame.multiplayer.mmo_server import *  # MMOServer
```

---

## ☁️ Облачные технологии (Cloud)

```python
from pywrkgame.cloud import *                        # Все облачные компоненты
from pywrkgame.cloud.streaming_optimization import * # StreamingOptimization
```

---

## 📊 Бенчмарки и профилирование (Benchmarks)

```python
from pywrkgame.benchmarks import *                    # Все бенчмарки
from pywrkgame.benchmarks.benchmark_runner import *   # BenchmarkRunner, BenchmarkResult
from pywrkgame.benchmarks.performance_profiler import *  # PerformanceProfiler
from pywrkgame.benchmarks.memory_profiler import *    # MemoryProfiler
from pywrkgame.benchmarks.rendering_benchmarks import *  # RenderingBenchmarks
from pywrkgame.benchmarks.raytracing_benchmarks import *  # RayTracingBenchmarks
from pywrkgame.benchmarks.platform_benchmarks import *   # PlatformBenchmarks
from pywrkgame.benchmarks.competitor_tests import *      # CompetitorBenchmarks
from pywrkgame.benchmarks.extreme_performance_test import *  # ExtremePerformanceTest
```

---

## 🛠️ Инструменты и утилиты (Tools & Utils)

### Утилиты
```python
from pywrkgame.utils import *              # Все утилиты
from pywrkgame.utils.vector import *       # Vec2, Vec3, Vec4
from pywrkgame.utils.matrix import *       # Matrix3, Matrix4, MatrixUtils
from pywrkgame.utils.color import *        # Color, ColorUtils
```

### Инструменты разработки
```python
from pywrkgame.tools import *              # Все инструменты
```

### Отладка
```python
from pywrkgame.debug import *              # DebugRenderer, Console, Logger
```

### Редактор
```python
from pywrkgame.editor import *             # Все компоненты редактора
from pywrkgame.editor.scene_editor import *  # SceneEditor
```

### UI система
```python
from pywrkgame.ui import *                 # Все UI компоненты
```

---

## 📱 Мобильная поддержка (Mobile)

```python
from pywrkgame.mobile import *             # Все мобильные компоненты
```

---

## 🔧 Интеграции (Integrations)

```python
from pywrkgame.integrations import *       # Все интеграции
```

---

## 🎯 Рекомендуемые импорты для начинающих

### Базовый набор
```python
from pywrkgame import *                    # Engine, Scene, GameConfig, quick_start
from pywrkgame.graphics import *           # Renderer, Colors
from pywrkgame.input import *              # Keyboard, Mouse
from pywrkgame.utils import *              # Vec2, Vec3, Color
```

### Для 2D игр
```python
from pywrkgame import *
from pywrkgame.graphics import *
from pywrkgame.graphics.sprite_renderer import *
from pywrkgame.input import *
from pywrkgame.physics import *
from pywrkgame.audio import *
```

### Для 3D игр
```python
from pywrkgame import *
from pywrkgame.graphics import *
from pywrkgame.graphics.raytracing import *
from pywrkgame.physics import *
from pywrkgame.input import *
from pywrkgame.audio import *
```

### Для VR игр
```python
from pywrkgame import *
from pywrkgame.graphics import *
from pywrkgame.vr import *
from pywrkgame.input import *
```

### Для Web3 игр
```python
from pywrkgame import *
from pywrkgame.graphics import *
from pywrkgame.web3 import *
from pywrkgame.multiplayer import *
```

---

## ⚠️ Важные замечания

1. **Производительность**: Импорт `*` может замедлить загрузку. Для продакшена используйте точечные импорты.

2. **Конфликты имен**: При использовании `import *` из нескольких модулей могут возникнуть конфликты имен.

3. **Рекомендация**: Для больших проектов используйте:
   ```python
   import pywrkgame as pwg
   from pywrkgame.graphics import Renderer
   from pywrkgame.input import Keyboard
   ```

4. **Автодополнение**: Многие IDE лучше работают с точечными импортами.

---

## 🚀 Быстрый старт

Для быстрого прототипирования:
```python
from pywrkgame import *
from pywrkgame.graphics import *
from pywrkgame.input import *

class MyGame(Scene):
    def render(self, renderer):
        renderer.clear(Colors.BLUE)

quick_start(MyGame)
```

---

*Справочник обновлен для PyWRKGame v2.1.0*