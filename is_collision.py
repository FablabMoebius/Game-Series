  def is_collision(self, player):
      if self.position_x == player.position_x:
          player.life -= self.damage
          return True
      return False
