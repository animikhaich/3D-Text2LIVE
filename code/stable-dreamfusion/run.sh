python3 main.py -O --text 'a standing stanford bunny' --workspace stanford_bunny --iters 50000 --lr 1e-3 --w 32 --h 32 --seed 0 --lambda_entropy 1e-5 --ckpt scratch --save_mesh --albedo_iters 10000

python3 main.py -O --test --workspace stanford_bunny --save_mesh