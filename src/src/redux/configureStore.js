import { combineReducers, createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import users from "redux/modules/users";

const env = process.env.NODE_ENV; // process - a variable that watchs out all processes going on over redux

// Rather than loading it anytime, load it only in the development mode
if (env === "development"){
  const { logger } = require("redux-logger");
}

const reducer = combineReducers({
  users
});

let store = initialState => 
    createStore(reducer, applyMiddleware(...middlewares));

export default store();