import tkinter as tk
import random

WIDTH = 400
HEIGHT = 400
CELL_SIZE = 20
SPEED = 150  


class Point:
   
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Food:
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.position = None
        self.rect_id = None
    
    def spawn(self):
        """Generate food at random position"""
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        self.position = Point(x, y)
        
        if self.rect_id:
            self.canvas.delete(self.rect_id)
        
        self.rect_id = self.canvas.create_rectangle(
            x, y, x + CELL_SIZE, y + CELL_SIZE, 
            fill="red", outline="darkred"
        )
    
    def get_coords(self):
        
        return self.canvas.coords(self.rect_id)


class Snake:
   
    def __init__(self, canvas):
        self.canvas = canvas
        self.segments = []
        self.direction = "Right"
        self.create_body()
    
    def create_body(self):
        
        start_x = 5
        start_y = 5
        snake_length = 5
        
        for i in range(snake_length):
            x1 = (start_x - i) * CELL_SIZE
            y1 = start_y * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            segment = self.canvas.create_rectangle(
                x1, y1, x2, y2, 
                fill="green", outline="darkgreen"
            )
            self.segments.append(segment)
    
    def get_head_coords(self):
        
        return self.canvas.coords(self.segments[0])
    
    def move(self):
        """Move snake in current direction"""
        x1, y1, x2, y2 = self.get_head_coords()
        
       
        if self.direction == "Right":
            x1 += CELL_SIZE
            x2 += CELL_SIZE
        elif self.direction == "Left":
            x1 -= CELL_SIZE
            x2 -= CELL_SIZE
        elif self.direction == "Up":
            y1 -= CELL_SIZE
            y2 -= CELL_SIZE
        elif self.direction == "Down":
            y1 += CELL_SIZE
            y2 += CELL_SIZE
        
        # Wrap around screen edges
        x1, x2 = self._wrap_horizontal(x1, x2)
        y1, y2 = self._wrap_vertical(y1, y2)
        
        return x1, y1, x2, y2
    
    def _wrap_horizontal(self, x1, x2):
       
        if x1 >= WIDTH:
            return 0, CELL_SIZE
        elif x2 <= 0:
            return WIDTH - CELL_SIZE, WIDTH
        return x1, x2
    
    def _wrap_vertical(self, y1, y2):
        
        if y1 >= HEIGHT:
            return 0, CELL_SIZE
        elif y2 <= 0:
            return HEIGHT - CELL_SIZE, HEIGHT
        return y1, y2
    
    def add_head(self, x1, y1, x2, y2):
       
        new_head = self.canvas.create_rectangle(
            x1, y1, x2, y2, 
            fill="green", outline="darkgreen"
        )
        self.segments.insert(0, new_head)
    
    def remove_tail(self):
       
        tail = self.segments.pop()
        self.canvas.delete(tail)
    
    def is_eating(self, food_coords):
        """Check if head collides with food"""
        hx1, hy1, hx2, hy2 = self.get_head_coords()
        fx1, fy1, fx2, fy2 = food_coords
        return hx1 == fx1 and hy1 == fy1
    
    def check_self_collision(self):
      
        head_coords = self.get_head_coords()
        for segment in self.segments[1:]:
            if self.canvas.coords(segment) == head_coords:
                return True
        return False
    
    def change_direction(self, new_direction):
       
        opposite = {
            "Up": "Down", 
            "Down": "Up", 
            "Left": "Right", 
            "Right": "Left"
        }
        if opposite[self.direction] != new_direction:
            self.direction = new_direction


class GameController:
    
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)
        self.game_over = False
        
        self.food.spawn()
        self.setup_controls()
        self.game_loop()
    
    def setup_controls(self):
        """Bind keyboard controls"""
        self.root.bind("<Up>", lambda e: self.snake.change_direction("Up"))
        self.root.bind("<Down>", lambda e: self.snake.change_direction("Down"))
        self.root.bind("<Left>", lambda e: self.snake.change_direction("Left"))
        self.root.bind("<Right>", lambda e: self.snake.change_direction("Right"))
    
    def game_loop(self):
        """Main game loop"""
        if self.game_over:
            return
        
      
        x1, y1, x2, y2 = self.snake.move()
        self.snake.add_head(x1, y1, x2, y2)
        
       
        if self.snake.is_eating(self.food.get_coords()):
            self.food.spawn()
        else:
            self.snake.remove_tail()
        
       
        if self.snake.check_self_collision():
            self.end_game()
            return
        
        # Continue game loop
        self.root.after(SPEED, self.game_loop)
    
    def end_game(self):
        """Display game over message"""
        self.game_over = True
        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2,
            fill="red",
            font=("Arial", 24, "bold"),
            text="GAME OVER!",
        )


def main():
    """Entry point for the game"""
    root = tk.Tk()
    root.title("Snake Game")
    game = GameController(root)
    root.mainloop()


if __name__ == "__main__":
    main()