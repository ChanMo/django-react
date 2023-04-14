Django + React
==============

An easy way to use React with Django.

QuickStart
----------

Install
~~~~~~~

.. code:: bash

   pip install django-vite-react

Update Settings.py
~~~~~~~~~~~~~~~~~~

.. code:: python

   INSTALLED_APPS = [
       ...
       'react',
       ...
   ]

Setup Vite
~~~~~~~~~~

Create file package.json

.. code:: json

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
       "@vitejs/plugin-react": "^3.1.0",
       "vite": "^4.1.1"
     },
     "dependencies": {
       "react": "^18.2.0",
       "react-dom": "^18.2.0"      
     }
   }

Create file vite.config.js

.. code:: javascript

   import { defineConfig } from 'vite'
   import react from '@vitejs/plugin-react'

   // https://vitejs.dev/config/
   export default defineConfig({
     plugins: [react()],
     build: {
       outDir: 'static/dist/',
       manifest: true,
       rollupOptions: {
         input: [
           'components/app.jsx',
         ]
       }
     }
   })

Install npm package

.. code:: bash

   npm install
   npm run dev

Create your jsx file
~~~~~~~~~~~~~~~~~~~~

Example ``components/app.jsx``

.. code:: javascript

   import React from 'react';
   import ReactDom from 'react-dom/client';

   function App(props) {
     return (
       <h1>{props.title}</h1>
     )
   }

   const root = ReactDom.createRoot(document.getElementById("app"));
   root.render(
     <App {...window.props} />
   );

Use ReactMixin in your ClassView
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from django.views.generic import TemplateView
   from react.mixins import ReactMixin


   class IndexView(ReactMixin, TemplateView):
       app_root = 'components/app.jsx'
       def get_props_data(self):
           return {
               'title': 'Hello'
           }

Visit url in your brower
~~~~~~~~~~~~~~~~~~~~~~~~

http://localhost:8000/

Build js
~~~~~~~~

Before deploy, run ``yarn dev``,

Final Structure
---------------

::

   .
   ├── backend
   │   ├── asgi.py
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── db.sqlite3
   ├── manage.py
   ├── node_modules
   ├── package.json
   ├── todo
   │   ├── admin.py
   │   ├── apps.py
   │   ├── components
   │   │   └── todo.jsx
   │   ├── __init__.py
   │   ├── migrations
   │   │   └── __init__.py
   │   ├── models.py
   │   ├── tests.py
   │   ├── urls.py
   │   └── views.py
   ├── static
   │   └── dist
   │       ├── assets
   │       │   └── todo-1cc3d04a.js
   │       └── manifest.json
   └── vite.config.js  

Todo
----

-  [ ] easier to integrate
-  [ ] decorate function
