const path = require('path')
const webpack = require('webpack')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const { VueLoaderPlugin } = require('vue-loader')
// const { HotModuleReplacementPlugin } = require('webpack')

// require('dotenv').config()

module.exports = {
  entry: './src/app.js',
  context: path.resolve(__dirname, 'frontend'),
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'frontend/dist'),
    publicPath: '/'
  },
  module: {
    rules: [
      { test: /\.js$/, loader: 'babel-loader', exclude: /node_modules/ },
      { test: /\.css$/, loader: ['style-loader', 'css-loader'] },
      { test: /\.s(a|c)ss$/, loader: ['style-loader', 'css-loader', 'sass-loader', 'postcss-loader'] },
      { test: /\.vue$/, loader: 'vue-loader' }
      // {
      //   // ...
      //   use: [
      //     // ...
      //     {
      //       loader: 'postcss-loader',
      //       options: {
      //         ident: 'postcss',
      //         plugins: [
      //           require('tailwindcss'),
      //           require('autoprefixer')
      //         ]
      //       }
      //     }
      //   ]
      // }
    ]
  },
  devServer: {
    contentBase: path.resolve('src'),
    hot: true,
    open: true,
    port: 4000,
    watchContentBase: true,
    historyApiFallback: true,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        secure: false
      }
    }
  },
  plugins: [
    // new HotModuleReplacementPlugin(),
    new VueLoaderPlugin(),
    new webpack.HotModuleReplacementPlugin(),
    new HtmlWebpackPlugin({
      // add favicon here
      template: 'src/index.html',
      filename: 'index.html',
      inject: 'body'
    })
    // new webpack.EnvironmentPlugin(['MAPBOX_ACCESS_TOKEN'])
  ]
}