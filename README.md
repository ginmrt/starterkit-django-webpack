# starterkit-django-webpack

A starter kit for projects wishing to use Django, Webpack, npm scripts and some extra goodies.


## Included

- `Django` 1.11 using `Jinja2` templating
- `Webpack` 2 with a sane basic config structure
- Basic `npm` scripts/commands for prod building and development
- HMR (Hot Module Reloading) for CSS and Javascript for development
- Starter `nginx` and `uWSGI` configs for Production deployments
- Basic ready-to-go `ESLint` and `Babel` configs for working in Javascript es6


## Missing elements

I'm still working on this kit and projects in parallel, some using a similar structure.
I haven't had the time to include everything I wanted yet so I'll likely make
some updates to the repo.

- SASS processing, webpack configs, sample files
- JS framework (I might add `React` or `Vue.js`), webpack configs, sample files
- Javascript test setup and accompanying `npm` scripts
- Python test setup (Will add `py.test` and `factory-boy` combo)
- Some extra goodies such as CSS autoprefixing, CI files, etc.


## Installation

Create a new virtualenv:
```
virtualenv ~/myappvenv
```

On Posix systems:
```
source ~/myappvenv/bin/activate
```

On Windows:
```
\Path\to\myappvenv\Scripts\activate
```

`cd` into the project's directory and:
```
# Install Python dependencies
pip install -r requirements/dev.txt

# Install npm dependencies
npm install
```

Run `Django`:
```
python manage.py runserver
```

In another terminal, `cd` into the project's directory and run `webpack-dev-server`:
```
npm run dev
```

Begin coding, test HMR is working, adjust the project to your needs.


## For Production

Not wanting to be too opinionated here, just giving the basics:

`cd` into the project's directory and:
```
# Django and Python stuff
pip install -r requirements.txt

# Frontend stuff
npm install --only=production
npm run build
python manage.py collectstatic
```


## Caveats

### Static files

Since this is using the [django-webpack-loader](https://github.com/owais/django-webpack-loader) package,
in which you render JS and CSS bundles from the HTML templates, I haven't used Webpack's `html-loader` or
`html-webpack-plugin`, which are used to inject the proper loading of generated assets files.

What this means, mostly, is that any image included in the HTML with an `<img>` tag will not be
managed/bundled by webpack (unless using a workaround as described below).

Static files under the `/webpack` directory in every app directory (`myapp`, `myblog`)
will be bundled by webpack (if 'required' correctly from a recognized script file
listed in the `entry` configuration element of `webpack.config.base.babel.js`).
The bundles created by webpack for these will be placed in the `assets` folder
when using the `npm run build` command. `Django`'s `collectstatic` command
will collect them from there during the Production build/deployment procedure.

Static files under the `/static` directory in every app directory (`myapp`, `myblog`)
will NOT be bundled by webpack. `Django`'s `collectstatic` command
will collect them from where they are during the Production build/deployment procedure.

As it stands, you have three options for `<img>` tags. There are examples for each one inside the
repo's included demo app. The first two options ensure the image is handled by webpack:

- #1- Use the image as a background in CSS rather than using an `<img>` tag

    Since webpack will take care of bundling your CSS and all calls to images using `url()`
therein, that is an option.

- #2- Import the image in a bundled Javascript file and load it from there

    The downside of this is a bug might prevent your image from being loaded and possibly visible delay
    in the actual loading when it works.

With this option, the image is not managed by webpack:

- #3- Use Django's standard `static` call

    Assuming `h1grumpy.png` is in `myapp/static/img/h1grumpy.png`.

    Use this in the HTML (`myapp/templates/base.html.j2`):
    ```
    <img class="img" src="{{ static('img/h1grumpy.png') }}" title="Very Grumpy"/>
    ```

### Cache busting and hash in webpack's assets filenames

Because of the static files situation, Webpack's insertion of hashes in filenames
for cache busting of static files in production was not a reliable option.

The package [django-static-url](https://github.com/resulto/django-static-url),
its usage in `Django`'s settings files and the addition of a related `nginx` location block
in the provided `nginx` config file are used for this instead.

In production, the principle is that a new hash would be generated on every deployment.

### ngrok

While running `webpack-dev-server` on `localhost:3000` with HMR activated and
`Django` on `localhost:8000`, if you run an ngrok command on top of it all in
a third terminal:

1. The HTTPS link ngrok will provide won't be able to load assets from
`webpack-dev-server`. A likely solution would be to locally build
everything "like production" and only run the `Django` server.

2. The regular HTTP link will work, but not the HMR. Hard refreshes will
be needed to see changes that you would see live on the locally running
link.

I'm sure there's some Browserify trickery to be done with this
but I haven't played enough with that to include something in the repo just yet.
Having a more elaborate ngrok config might also fix these issues.

More details to come on this section after I've had the time to try it more.


## Some notes

### Server configs

- The provided `nginx` config is specific to the project and doesn't include
the base config typically located under `/etc/nginx/nginx.conf`.
- The provided `uWSGI` config is specific to the project and doesn't include
a `uWSGI` emperor service file or anything else.

### Static files

The kit, including server configs, assumes static files will be served
from the same server as the `Django` website.


## Extra Reading

- [django-webpack-loader](https://github.com/owais/django-webpack-loader)
- [django-static-url](https://github.com/resulto/django-static-url)
