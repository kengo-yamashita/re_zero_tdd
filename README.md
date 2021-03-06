# Re:ゼロから始めるテスト駆動開発

[![Floobits Status](https://floobits.com/k2work/re_zero_tdd.svg)](https://floobits.com/k2work/re_zero_tdd/redirect)
[![CircleCI](https://circleci.com/gh/hiroshima-arc/re_zero_tdd.svg?style=svg)](https://circleci.com/gh/hiroshima-arc/re_zero_tdd)
[![Test Coverage](https://api.codeclimate.com/v1/badges/37c77902165bbea35337/test_coverage)](https://codeclimate.com/github/hiroshima-arc/re_zero_tdd/test_coverage)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0f501f7150dc4ffb9a6768847f074c7e)](https://www.codacy.com/app/kakimomokuri/re_zero_tdd?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=hiroshima-arc/re_zero_tdd&amp;utm_campaign=Badge_Grade)
[![codebeat badge](https://codebeat.co/badges/af73d155-80e3-48f5-b820-b75a7b8303fb)](https://codebeat.co/projects/github-com-hiroshima-arc-re_zero_tdd-master)

## 目的

実践テスト駆動開発

## 前提

| ソフトウェア       | バージョン | 備考 |
| :----------------- | :--------- | :--- |
| Visual Studio Code |            |      |
| vagrant            | 2.0.3      |      |
| Ruby               | 2.5.3      |      |
| Node.js            | 8.10.0     |      |
| Python             | 3.6.0      |      |
| Elixir             | 1.7.4      |      |
| Erlang             | 21.1.1     |      |

## 構成

1. [構築](#構築)
1. [配置](#配置)
1. [運用](#運用)
1. [開発](#開発)

### 構築

#### エディタの用意

- [Visual Studio Code のインストール](https://code.visualstudio.com/)
- [VS Live Share Extension Pack のセットアップ](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-pack)

#### 開発用仮想マシンの起動・プロビジョニング

```bash
vagrant up
vagrant ssh
```

#### ドキュメント環境構築セットアップ

```bash
curl -s api.sdkman.io | bash
source "/home/vagrant/.sdkman/bin/sdkman-init.sh"
sdk list maven
sdk use maven 3.5.4
sdk list java
sdk use java 8.0.181-zulu
sdk list gradle
sdk use gradle 4.10
```

#### 開発パッケージのセットアップ

##### 共通ライブラリのセットアップ

```
sudo yum update -y
sudo yum install -y build-essential \
                   libssl-dev \
                   gcc-c++  \
                   openssl-devel  \
                   bzip2-devel  \
                   zlib-devel  \
                   readline-devel  \
                   sqlite-devel  \
                   python-devel  \
                   python3-dev  \
                   automake  \
                   autoconf  \
                   ncurses-devel
```

##### Ruby のセットアップ

- rbenv のインストール
- ruby-build のインストール
- Ruby のインストール

```bash
cd /vagrant
git clone https://github.com/sstephenson/rbenv ~/.rbenv
git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
sudo ~/.rbenv/plugins/ruby-build/install.sh
echo 'export PATH="~/.rbenv/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(rbenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
rbenv install --list
rbenv install 2.5.3
rbenv local 2.5.3
```

##### Node.js のセットアップ

- nvm のインストール
- Node.js のインストール

```bash
cd /vagrant
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.3/install.sh | bash
source ~/.bashrc
nvm install v8.10
nvm alias default v8.10
```
##### Python のセットアップ

- pyenv のインストール
- Python のインストール

```bash
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

`~/.bashrc`に以下を追加して`source ~/.bashrc`

```
export PATH="/home/vagrant/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

利用する Python のバージョンをインストールする

```
cd /vagrant
pyenv install -l
pyenv install 3.6.0
pyenv local 3.6.0
```

##### Elixir のセットアップ

- asdf のインストール
- Erlang のインストール
- Elixir のインストール

```bash
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.6.0
echo -e '\n. $HOME/.asdf/asdf.sh' >> ~/.bashrc
echo -e '\n. $HOME/.asdf/completions/asdf.bash' >> ~/.bashrc
```

シェルに再ログインする

利用する asdf のプラグインをインストール

```
asdf plugin-add erlang
asdf plugin-add elixir
```

利用する Elixir と Erlang をインストール

注意 利用する Elixir によって利用可能な Erlang のバージョンが違います。
参考 [Compatibility between Elixir and Erlang/OTP](https://hexdocs.pm/elixir/compatibility-and-deprecations.html#compatibility-between-elixir-and-erlang-otp)

```
cd /vagrant
asdf list-all erlang
asdf install erlang 21.1.1
asdf local erlang 21.1.1
asdf list-all elixir
asdf install elixir 1.7.4
asdf local elixir 1.7.4
```

##### PHP のセットアップ

- phpenv のインストール
- PHP のインストール

```bash
export PHP_VER=7.3.0
git clone https://github.com/CHH/phpenv.git
phpenv/bin/phpenv-install.sh
git clone git://github.com/CHH/php-build.git $HOME/.phpenv/plugins/php-build
sudo yum --enablerepo=epel install re2c libmcrypt libmcrypt-devel
sudo yum install libxml2-devel bison bison-devel openssl-devel curl-devel libjpeg-devel libpng-devel libmcrypt-devel readline-devel libtidy-devel libxslt-devel httpd-devel enchant-devel libXpm libXpm-devel freetype-devel t1lib t1lib-devel gmp-devel libc-client-devel libicu-devel oniguruma-devel net-snmp net-snmp-devel bzip2-devel
```

`~/.bashrc`に以下を追加して`source ~/.bashrc`

```
echo 'export PATH="/$HOME/.phpenv/bin:$PATH"' >> $HOME/.bash_profile
echo 'eval "$(phpenv init -)"' >> $HOME/.bash_profile
```

利用する PHP のバージョンをインストールする

```
cd /vagrant
phpenv install -l
phpenv install $PHP_VER
phpenv global $PHP_VER
```



#### CI 環境のセットアップ

##### CI 用イメージのビルド

```
vagrant up
vagrant ssh
cd /vagrant
docker build -t re-zero-tdd . -f ops/Dockerfile
docker tag re-zero-tdd:latest hiroshimaarc/re-zero-tdd:1.0.0
```

##### イメージのプッシュ

```
docker login
docker push hiroshimaarc/re-zero-tdd:1.0.0
```

##### circleci コマンドのインストール

```
sudo curl -fLSs https://circle.ci/cli | bash
circleci update
```

##### circleci 設定ファイルの作成

```
mkdir .circleci
touch .circleci/config.yml
```

**[⬆ back to top](#構成)**

### 配置

ドキュメントの生成

```
cd /vagrant
gradle build
gradle asciidoctor
gradle livereload
```

[http://localhost:35729/](http://localhost:35729/)に接続して確認する

**[⬆ back to top](#構成)**

### 運用

#### circleci

##### local 環境で circleci を動かす

```
vagrant up
vagrant ssh
cd /vagrnt
circleci config validate -c .circleci/config.yml
circleci build .circleci/config.yml
```

#### Prettier

マークダウンファイルのフォーマットをする

インストール

```
npm install --save-dev --save-exact prettier
```

実行

```
npm run format
```

#### remarklint

マークダウンファイルのコードチェックをする

インストール

```
npm install -g --save remark-cli remark-preset-lint-recommended
```

実行

```
npm run check
```

#### ESlint

マークダウンファイルのコードチェックをする

インストール

```
npm install -g eslint-cli
npm install --save-dev eslint
npx eslint --init 
```

実行

```
npm run lint
```

**[⬆ back to top](#構成)**

### 開発

#### README.md ファイルのセットアップ

```
vagrant ssh
cd /vagrant
rake doc:setup
```

#### Python 開発環境

```
vagrant ssh
cd /vagrant
docker-compose up env-python
```

[http://127.0.0.1:6901/?password=guest](http://127.0.0.1:6901/?password=guest)

#### Ruby 開発環境

```
vagrant ssh
cd /vagrant
docker-compose up env-ruby
```

[http://127.0.0.1:6901/?password=guest](http://127.0.0.1:6901/?password=guest)

**[⬆ back to top](#構成)**

## 参照

- [AWS SAM Node.js Hands-on](https://github.com/hiroshima-arc/aws_sam_nodejs_hands-on)
- [AWS SAM Python Hands-on](https://github.com/hiroshima-arc/aws_sam_python_hands-on)
- [circleci](https://circleci.com/)
- [docker cloud](https://cloud.docker.com/u/hiroshimaarc/repository/docker/hiroshimaarc/re-zero-tdd)
- [Prettier](https://prettier.io/)
- [remarklint](https://github.com/remarkjs/remark-lint)
- [ESLint 最初の一歩](https://qiita.com/mysticatea/items/f523dab04a25f617c87d)
- [新しくなった eslint --init を試す](https://qiita.com/mysticatea/items/e2cd8b2c9879b3b0f561)

## このリポジトリへの参加方法

このリポジトリへコミットやプルリクエストを作成するには、[CONTRIBUTING.md](CONTRIBUTING.md) をお読み下さい。
