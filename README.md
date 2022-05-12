# Django + React

Use Vite


## QuickStart

### Install

```
```

### Update Settings.py

```
INSTALLED_APPS = [
    ...
    'react',
    ...
]
```

### Setup Vite

Create file package.json
```
{
  "name": "django-react",
  "version": "1.0.0",
  "description": "use react.js in django templates",
  "main": "index.js",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "ChanMo",
  "license": "ISC",
  "devDependencies": {
    "@vitejs/plugin-react": "^1.2.0",
    "vite": "^2.8.6"
  },
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2"
  }
}
```

Create file vite.config.js

```
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'backend/static/backend/dist/',
    manifest: true,
    rollupOptions: {
      input: [
	    'yourreactfile.jsx',
      ]
    }
  }
})

```

Install npm package

```
$ npm install
$ npm run dev
```

### Create your jsx file

Example `backend/components/app.jsx`

```
import React from 'react'
import ReactDOM from 'react-dom'


function App(props) {
  return (
    <h1>{props.title}</h1>
  )
}

ReactDOM.render(
  <React.StrictMode>
    <App {...window.props} />
  </React.StrictMode>,
  document.getElementById("app")
)
```

### Use ReactMixin in your ClassView

```
from django.views.generic import TemplateView
from react.mixins import ReactMixin


class IndexView(ReactMixin, TemplateView):
    app_root = '/backend/components/app.jsx'
    def get_props_data(self):
        return {
            'title': 'Hello'
        }
```

### Visit url in your brower

### Build js

Before prepare to deploy, run `yarn dev`,


## Todo

* [ ] easier to integrate
* [ ] decorate function
