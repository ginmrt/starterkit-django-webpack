import '../css/myblog.css';
import imgGithub from '../img/githubw256.png';

// Importing and loading an image in JS instead of using an <img> tag to force
// Webpack to manage the image file and possibly inline it into the bundle
// if it is small enough (see `url-loader` usage in webpack config).
const github = document.getElementById('github');
github.src = imgGithub;
