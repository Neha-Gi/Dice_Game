from Dice_board_base import DummyDice
import sys
class Game:
    def __init__(self, num_of_players: int):
        self.num_of_players = num_of_players
        self.players = [input(f"Enter name for Player {i+1}: ") for i in range(num_of_players)]
        self.player_scores = [0] * num_of_players
        self.current_player_index = 0
        self.current_player_dice = DummyDice()

    def next_player(self) -> None:
        self.current_player_index = (self.current_player_index + 1) % self.num_of_players

    def play_turn(self) -> None:
        current_player = self.players[self.current_player_index]
        input(f"{current_player}, press Enter to roll the dice...")

        self.current_player_dice.roll()
        print(f'{current_player} rolled:')
        self.display_dice(self.current_player_dice.total)

        total_points = self.current_player_dice.total
        
        if total_points in [ 4]:
                self.player_scores[self.current_player_index] = 0
                print(f"{current_player} has got {total_points} points and resets to zero :( :( :( ")
        elif total_points in[8]:
                self.player_scores[self.current_player_index] =int(self.current_player_dice.total) *2    
                print(f"{current_player} has got {total_points} points and get double points !!!!!")
        else:
                self.player_scores[self.current_player_index] += total_points
                print(f"{current_player} rolled: {total_points}. Total score: {self.player_scores[self.current_player_index]}")

        if self.player_scores[self.current_player_index] >= 50:
            self.announce_winner()
            sys.exit()

        self.next_player()

    def announce_winner(self) -> None:
        max_score = max(self.player_scores)
        if max_score >= 50:
            winner_index = self.player_scores.index(max_score)
            winner_name = self.players[winner_index]
            
            print(f"The winner is {winner_name} with {max_score} points :) :) :) !\n\n***CONGRATULATIONS {winner_name}***\n")
    
    @staticmethod
    def display_dice(face: int) -> None:
        patterns = {
            1: [" ------- ", "|       |", "|   *   |", "|       |", " ------- "],
            2: [" ------- ", "| *     |", "|       |", "|     * |", " ------- "],
            3: [" ------- ", "| *     |", "|   *   |", "|     * |", " ------- "],
            4: [" ------- ", "| *   * |", "|       |", "| *   * |", " ------- "],
            5: [" ------- ", "| *   * |", "|   *   |", "| *   * |", " ------- "],
            6: [" ------- ", "| * * * |", "|       |", "| * * * |", " ------- "],
            7: [" ------- ", "| * * * |", "|   *   |", "| * * * |", " ------- "],
            8: [" ------- ", "| * * * |", "| * * * |", "| * * * |", " ------- "],
        }

        print("\n".join(patterns[face]))