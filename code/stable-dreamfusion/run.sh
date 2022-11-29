python3 main.py -O --text 'a DSLR photo of a squirrel' --workspace squirrel --iters 100000 --lr 1e-3 --w 64 --h 64 --seed 333 --lambda_entropy 1e-5 --ckpt scratch --save_mesh --albedo_iters 10000

python3 main.py -O --test --workspace squirrel --save_mesh