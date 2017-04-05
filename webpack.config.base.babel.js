import path from 'path';
import webpack from 'webpack';

export default {
  context: __dirname,
  entry: {
    // Separate bundle for Vendor CSS
    vendorcss: path.resolve('./myapp/webpack/js/vendorcss.js'),
    // Add all entry points here, aka all apps
    base: path.resolve('./myapp/webpack/js/base.js'),
    myblog: path.resolve('./myblog/webpack/js/myblog.js'),
  },
  target: 'web',
  output: {
    path: path.resolve('./assets/bundles/'),
    filename: '[name].js',
  },
  plugins: [
    // 3rd party css
    new webpack.optimize.CommonsChunkPlugin({
      name: 'vendorcss',
    }),
    // 3rd party js
    new webpack.optimize.CommonsChunkPlugin({
      name: 'vendorjs',
      minChunks(module) {
        // This assumes all vendor imports exist in the node_modules directory
        return module.context && module.context.indexOf('node_modules') !== -1;
      },
    }),
    // Separate Webpack manifest file to avoid false positive change detections in js
    new webpack.optimize.CommonsChunkPlugin({
      name: 'manifest',
    }),
  ],
  module: {
    rules: [
      {
        test: /\.(png|jpg|jpeg|gif|svg|woff|woff2|eot|ttf|otf)$/,
        use: [
          {
            loader: 'url-loader',
            options:
            {
              limit: 8192,
              name: '[name].[ext]',
            },
          },
        ],
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader', // Do not use "use" here
        query: {
          presets: ['env'],
        },
      },
    ],
  },
  node: {
    console: true,
    fs: 'empty',
    net: 'empty',
    tls: 'empty',
    child_process: 'empty',
    module: 'empty',
  },
};
