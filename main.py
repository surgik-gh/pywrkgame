"""
PyWRKGame 3.0.0 - Android Entry Point
This file serves as the entry point for Android builds using Buildozer
"""

import sys
import os

# Add python directory to path
python_dir = os.path.join(os.path.dirname(__file__), 'python')
if os.path.exists(python_dir):
    sys.path.insert(0, python_dir)

try:
    # Import PyWRKGame
    import pywrkgame as pwg
    from pywrkgame_api import quick_game
    
    print("PyWRKGame 3.0.0 initialized successfully!")
    print(f"Platform: {sys.platform}")
    print(f"Python version: {sys.version}")
    
    # Create a simple demo game
    def run_demo():
        """Run a simple demo game"""
        game = quick_game("PyWRKGame Demo")
        
        # Create a simple sprite
        player = game.create_sprite("player.png", 640, 360)
        
        # Setup update callback
        @game.on_update
        def update(dt):
            # Simple movement based on input
            speed = 200
            player.move(
                game.input.x * speed * dt,
                game.input.y * speed * dt
            )
        
        print("Demo game created. Ready to run!")
        # Note: game.run() would be called here in a real application
        # For Android, this would start the main game loop
        
        return game
    
    if __name__ == "__main__":
        print("Starting PyWRKGame demo...")
        demo_game = run_demo()
        print("Demo game initialized. Use game.run() to start.")
        
except ImportError as e:
    print(f"Error importing PyWRKGame: {e}")
    print("Make sure the C++ bindings are built correctly.")
    print("For Android builds, ensure all native libraries are included.")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
