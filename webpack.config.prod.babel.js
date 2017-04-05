import webpack from 'webpack';
import BundleTracker from 'webpack-bundle-tracker';
import UglifyJSPlugin from 'webpack-uglify-harmony';
import ExtractTextPlugin from 'extract-text-webpack-plugin';

import config from './webpack.config.base.babel';

config.devtool = 'source-map';

config.plugins = config.plugins.concat([
  // Generate separate css files
  new ExtractTextPlugin('[name].css'),
  new BundleTracker({ filename: './webpack-stats-prod.json' }),

  new webpack.DefinePlugin({
    'process.env': { NODE_ENV: JSON.stringify('production') },
  }),

  // Minify JS
  new UglifyJSPlugin({
    sourceMap: true,
    compressor: {
      warnings: false,
    },
  }),
]);

config.module.rules.push(
  {
    test: /\.css$/,
    use: ExtractTextPlugin.extract({
      use: [
        {
          loader: 'css-loader',
          options: {
            minimize: true,
          },
        },
      ],
    }),
  });

export default config;
