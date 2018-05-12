"use strict";
const webpack = require('webpack');
const path = require('path');
const root = path.join(__dirname, './');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const autoprefixer = require('autoprefixer');
const precss = require('precss');

module.exports = [
  {
    entry: {
      common: path.join(root, 'src/js/common.js'),
      members: path.join(root, 'src/js/members.js'),
      //vendor: ['jquery', 'tether', 'bootstrap'],
      //vendor: ['moment'],
    },
    output: {
      path: path.join(root, 'app/statics/js'),
      filename: '[name].js'
    },
    optimization: {
      splitChunks: {
        name: 'vendor',
        chunks: 'initial',
      }
    },
    resolve: {
      extensions: ['.webpack.js', '.web.js', '.js'],
      alias: {
        'vue$': 'vue/dist/vue.common.js',
        'vue-router$': 'vue-router/dist/vue-router.common.js'
      }
    },
    module: {
      rules: [
        {
          test: /\.css/,
          use: [
            'style-loader',
            {loader: 'css-loader', options: {url: false}},
          ],
        }
      ]
    },
    plugins: [
      // Ignore all locale files of moment.js
      new webpack.IgnorePlugin(/^\.\/locale$/, /moment$/),
      //// webpack.ProvidePluginを使用すると、指定した変数名でライブラリを使用できるようになる
      //new webpack.ProvidePlugin({
      //  $: 'jquery',
      //  jQuery: 'jquery',
      //  'window.jQuery': 'jquery'
      //}),
      //new webpack.ProvidePlugin({
      //  moment: 'moment'
      //})
    ],
    devtool: 'source-map',
  },
  {
    entry: {
      common: path.join(root, 'src/scss/common.scss'),
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
      new ExtractTextPlugin('common.css'),
    ],
    devtool: 'source-map',
    resolve: {
      extensions: ['.scss']
    },
  }
];
