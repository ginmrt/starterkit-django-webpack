import chalk from 'chalk';
import webpack from 'webpack';
import webpackConfig from '../webpack.config.prod.babel';

console.log('------------------------------');
console.log(chalk.blue('Running webpack for production. This will take a moment...'));

webpack(webpackConfig).run((err, stats) => {
  if (err) {
    console.log(chalk.red(err));
    return 1;
  }
  const jsonStats = stats.toJson();
  if (jsonStats.hasErrors) {
    console.log('------------------------------');
    return jsonStats.errors.map(error => console.log(chalk.red(error)));
  }

  if (jsonStats.hasWarnings) {
    console.log('------------------------------');
    console.log(chalk.yellow('Webpack generated the following warnings: '));
    jsonStats.warnings.map(warning => console.log(chalk.yellow(warning)));
  }
  console.log('------------------------------');
  console.log(chalk.cyan('Webpack stats: '));
  console.log(`${stats}`);
  console.log('------------------------------');

  console.log(chalk.green('Production build complete.'));
  return 0;
});
