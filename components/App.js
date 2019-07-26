import { createElement as h, Fragment } from 'react';

const makeDummyRequest = () =>
  fetch('/test', { method: 'GET' }).then(r => r.json().then(j => console.log(j)));

const App = () =>
  h(
    Fragment,
    null,
    h('h1', null, 'Flask + React + SKLearn fun'),
    h('button', { onClick: makeDummyRequest }, 'Test'),
  );

export default App;
