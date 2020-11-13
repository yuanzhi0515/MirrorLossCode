import os
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('--env', default='Frostbite')
parse.add_argument('--seed', default=0)
parse.add_argument('--mirror', default=False, action='store_true')
args = parse.parse_args()

commond = 'python -m baselines.run --alg=deepq --env={env_name}NoFrameskip-v4 --seed={seed} --num_timesteps=1e7'.format(env_name=args.env, seed=args.seed)
if args.mirror == True:
    log_path = ' --log_path=/data/DQN/logs/{env_name}-DQN-mirror-lr/seed-{seed}'.format(env_name=args.env, seed=args.seed)
    save_path = ' --save_path=/data/DQN/models/{env_name}-DQN-models-mirror-lr/seed-{seed}'.format(env_name=args.env, seed=args.seed)
    commond += ' --mirror'
else:
    log_path = ' --log_path=/data/DQN/logs/{env_name}-DQN/seed-{seed}'.format(env_name=args.env, seed=args.seed)
    save_path = ' --save_path=/data/DQN/models/{env_name}-DQN-models/seed-{seed}'.format(env_name=args.env, seed=args.seed)
print(commond + log_path + save_path)
total_commond = commond + log_path + save_path
os.system(total_commond)
