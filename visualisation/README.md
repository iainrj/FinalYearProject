## Development Workflow

**1. Start a live-reload development server:**

```sh
npm run dev
```

> This is a full web server nicely suited to your project. Any time you make changes within the `src` directory, it will rebuild and even refresh your browser.

**2. Testing with `mocha`, `karma`, `chai`, `sinon` via `phantomjs`:**

```sh
npm test
```

> 🌟 This also instruments the code in `src/` using [isparta](https://github.com/douglasduteil/isparta), giving you pretty code coverage statistics at the end of your tests! If you want to see detailed coverage information, a full HTML report is placed into `coverage/`.

**3. Generate a production build in `./build`:**

```sh
npm run build
```

> You can now deploy the contents of the `build` directory to production!
>
> **[Surge.sh](https://surge.sh) Example:** `surge ./build -d my-app.surge.sh`
> 
> **[Netlify](https://www.netlify.com/docs/cli/) Example:** `netlify deploy`
>
> [![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/developit/preact-boilerplate)


**4. Start local production server with [serve](https://github.com/zeit/serve):**

```sh
npm start
```

> This is to simulate a production (CDN) server with gzip. It just serves up the contents of `./build`.
