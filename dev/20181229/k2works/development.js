/*eslint no-undef: "error"*/
/*eslint-env node*/

import path from "path";
import HtmlWebpackPlugin from "html-webpack-plugin";

const src = path.resolve(__dirname, "src");
const dist = path.resolve(__dirname, "dist");

module.exports = {
  mode: "development",
  entry: ["./src/index.jsx"],

  output: {
    path: dist,
    filename: "main.js"
  },

  devServer: {
    contentBase: src,
    open: true
  },

  module: {
    rules: [
      {
        test: [/\.js$/, /\.jsx$/],
        use: [
          {
            loader: "babel-loader",
            options: {
              presets: [
                "@babel/preset-env",
                "@babel/react"
              ]
            }
          }
        ]
      },
      {
        test: /\.css$/,
        loaders: ["style-loader", "css-loader?modules"],
      }
    ]
  },

  resolve: {
    extensions: [".js", ".jsx", ".scss", ".css", ".html"],
    modules: ["node_modules"]
  },

  plugins: [
    new HtmlWebpackPlugin({
      template: src + "/index.html",
      filename: "index.html"
    })
  ]
};