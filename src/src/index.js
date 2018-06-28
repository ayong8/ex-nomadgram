import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from "react-redux";
import store from "redux/configureStore";

import App from 'components/App';

//const store = configureStore();

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById("root")
);
