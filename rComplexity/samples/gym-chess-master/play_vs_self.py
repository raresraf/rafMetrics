import random

import gym
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage: python3 play_vs_self.py <num_episodes> <num_steps_per_episode>"
        )
        sys.exit(-1)

    env = gym.make('ChessVsSelf-v0')

    #num_episodes = 100
    num_episodes = int(sys.argv[1])
    #num_steps_per_episode = 80
    num_steps_per_episode = int(sys.argv[2])

    collected_rewards = {1: [], -1: []}

    for i in range(num_episodes):
        initial_state = env.reset()
        # print('<'*5, '='*10, 'NEW GAME {}'.format(i+1), '='*10, '>'*5)
        # env._render()
        # print('<'*5, '-'*10, 'STARTING', '-'*10, '>'*5)

        player1 = 1
        player2 = -1
        total_rewards = {1: 0, -1: 0}
        done = False

        for j in range(num_steps_per_episode):
            if done or j == (num_steps_per_episode - 1):
                print('TOTAL GAME ', i, 'REWARD =', total_rewards)
                break

            for player in [player1, player2]:
                state = env.state
                board = state['board']
                kr_moves = state['kr_moves']
                captured = state['captured']

                moves = env.get_possible_moves(state, player)

                if len(moves) == 0:
                    a = env.resign_action()
                    print('<' * 5, '@' * 10, 'PLAYER RESIGNED', '@' * 10,
                          '>' * 5)
                else:
                    m = random.choice(moves)
                    a = env.move_to_actions(m)
                    # print('{:6s}'.format(env.convert_coords(m)), end=' ')

                # perform action
                state, reward, done, __ = env.step(a)
                total_rewards[player] += reward

        collected_rewards[1].append(total_rewards[1])
        collected_rewards[-1].append(total_rewards[-1])

    reward_1 = sum(collected_rewards[1])
    reward_2 = sum(collected_rewards[-1])

    print('\n')
    print('#' * 40)
    print('#' * 40)
    print('#' * 40)
    print("\nAVERAGE SCORE PLAYER 1: ", reward_1 / num_episodes)
    print("AVERAGE SCORE PLAYER 2: ", reward_2 / num_episodes)
    print('\n')
