import path from 'path';
import webpack from 'webpack';
import BundleTracker from 'webpack-bundle-tracker';

import config from './webpack.config.base.babel';

config.devtool = 'inline-source-map';

// Apply Hot Module Reloading (HMR) in Dev
Object.assign(config.entry, {
  hmr: [
    // Include the client code. Note host/post.
    'webpack-dev-server/client?http://localhost:3000',

    // Hot reload only when compiled successfully
    'webpack/hot/only-dev-server',

    // Alternative with refresh on failure
    // 'webpack/hot/dev-server',
  ],
});

config.output.publicPath = 'http://localhost:3000/assets/bundles/';
config.devServer = {
  contentBase: path.join(__dirname, './assets/bundles/'),
  inline: true,
  host: '0.0.0.0',
  port: 3000,
  publicPath: config.output.publicPath,
  hot: true,
  quiet: false,
  historyApiFallback: true,
};

config.module.rules.push(
  {
    test: /\.css$/,
    use: ['style-loader', 'css-loader'],
  });

config.plugins = config.plugins.concat([
  new webpack.HotModuleReplacementPlugin(),
  new webpack.NoEmitOnErrorsPlugin(),
  new webpack.NamedModulesPlugin(),
  new BundleTracker({ filename: './webpack-stats-dev.json' }),
]);

export default config;
