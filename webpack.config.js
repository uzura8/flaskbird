"use strict";
const webpack = require('webpack');
const path = require('path');
const root = path.join(__dirname, './');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const autoprefixer = require('autoprefixer');
const precss = require('precss');

module.exports = [
  //{
  //  //entry: {
  //  //  //basic: path.join(root, 'src/js/basic.js'),
  //  //  //component: path.join(root, 'src/js/component.js'),
  //  //  //vendor: ['jquery', 'tether', 'bootstrap'],
  //  //  //app: path.join(root, 'src/js/app.js'),
  //  //},
  //  //output: {
  //  //  path: path.join(root, 'public/assets/js'),
  //  //  filename: '[name].js'
  //  //},
  //  resolve: {
  //    extensions: ['.webpack.js', '.web.js', '.js'],
  //    alias: {
  //      'vue$': 'vue/dist/vue.common.js',
  //      'vue-router$': 'vue-router/dist/vue-router.common.js'
  //    }
  //  },
  //  plugins: [
  //    // この設定をするとvendorの中身は他のentryでは読み込まれない
  //    new webpack.optimize.CommonsChunkPlugin('vendor'),
  //    // webpack.ProvidePluginを使用すると、指定した変数名でライブラリを使用できるようになる
  //    new webpack.ProvidePlugin({
  //      $: 'jquery',
  //      jQuery: 'jquery',
  //      'window.jQuery': 'jquery'
  //    }),
  //    new webpack.ProvidePlugin({
  //      'window.Tether': 'tether',
  //      Tether: "tether",
  //    }),
  //    //new webpack.ProvidePlugin({
  //    //    moment: 'moment'
  //    //})
  //  ],
  //  devtool: 'source-map',
  //},
  {
    entry: {
      bulma_custom: path.join(root, 'src/scss/bulma_custom.scss'),
    },
    output: {
      path: path.join(root, 'app/statics/css'),
      filename: '[name].css'
    },
    module: {
      rules: [{
        test: /\.scss$/,
        use: ExtractTextPlugin.extract(
          {
            use: [
              {
                loader: 'css-loader'
              },
              {
                loader: 'postcss-loader',
                options: {
                  plugins: (loader) => [
                    require('autoprefixer')()
                  ],
                  sourceMap: true
                }
              },
              {
                loader: 'sass-loader',
                options: {
                  outputStyle: 'compressed',
                  sourceMap: true
                }
              }
            ]
          }
        )
      }]
    },
    plugins: [
      new ExtractTextPlugin('bulma_custom.css'),
    ],
    devtool: 'source-map',
    resolve: {
      extensions: ['.scss']
    },
  }
];
