import argparse # python用来处理命令行参数的包
import yaml
from easydict import EasyDict

def parse_config():
    parser = argparse.ArgumentParser(description='arg parser')
    parser.add_argument('--la', type=str, default=None, help='specify the config for training')

    args = parser.parse_args()

    cfg_file = args.la          # 命令行参数就是配置文件
    with open(cfg_file,'r') as f:
        load_cfg = yaml.safe_load(f)
        cfg = EasyDict(load_cfg)
        #cfg = {}
        #cfg.update(load_cfg)
        #cfg.EasyDict()

    return args,cfg

def main():
    args,cfgs = parse_config()
    print(args.la)
    print(cfgs.DATA_CONFIG)   # 原本cfg就是一个字典，只能用['']来访问，使用easydict包，可以像访问属性一样访问字典的键值对



if __name__ == '__main__':
    main()
