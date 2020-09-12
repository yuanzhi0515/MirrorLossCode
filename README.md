# Code for "Improving Deep Reinforcement Learning with Mirror Loss" 
This repository contains the mirror loss implementation based on OpenAI Baselines. The installation is the same as original Baselines. 
## Train DRL agent with mirror loss
Note: Currently only implementations of ppo2 and deepq support mirror loss. Trainning agent with mirror loss in a Atari game needs the mirror correspondence of that environment. The repository supports traninning in BeamRider, Breakout, Enduro, Pong, Qbert and Seaquest. If you want to train you agent in other Atari games, you can modify the function ``baselines.commom.mirror_utils.mirror_modify``.
### Example 1. DQN with mirror loss in Breakout
```bash
python -m baselines.run --alg=deepq --env=BreakoutNoFrameskip-v4 --seed=0 --num_timesteps=1e7 --log_path=YOUR_LOG_PATH --save_path=YOUR_SAVE_PATH --mirror
```
If you don't want to use default mirror loss coefficient, you can add: ``--mirror_coef=YOUR_SET``
### Example 2. PPO with mirror loss in Breakout
```bash
python -m baselines.run --alg=ppo2 --env=BreakoutNoFrameskip-v4 --num_env=8 --seed=0 --num_timesteps=1e7 --log_path=YOUR_LOG_PATH --save_path=YOUR_SAVE_PATH --mirror
``` 
If you don't want to use default policy mirror loss coefficient and value mirror loss coefficient, you can add:
``--policy_mirror_coef=YOUR_POLICY_SET --value_mirror_coef=YOUR_VALUE_SET``
### Example 3. Test model trained by DQN with mirror loss in mirrored Breakout
```bash
python -m baselines.run --alg=deepq --env=BreakoutNoFrameskip-v4 --num_timesteps=0 --num_env=1 --load_path=YOUR_MODEL_PATH --play --mirror
```