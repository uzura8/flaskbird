from app import app
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--env', help='環境変数',
                    type=str, choices=['local', 'dev', 'stg', 'prd'],
                    default='local')
args = parser.parse_args()

# 起動時の引数毎に読み込ませる設定が異なる
env = args.env
if env == 'local':
    app.config.from_object('config.local.LocalConfig')
elif env == 'dev':
    app.config.from_object('config.development.DevelopmentConfig')
elif env == 'stg':
    app.config.from_object('config.staging.StagingConfig')
elif env == 'prd':
    app.config.from_object('config.production.ProductionConfig')
else:
    app.config.from_object('config.BaseConfig')

if __name__ == '__main__':
    app.run()

