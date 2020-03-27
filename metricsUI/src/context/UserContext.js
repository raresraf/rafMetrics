import React from "react";
import {backend_login_ip, backend_webmonitoringapi_ip} from '../config';

var UserStateContext = React.createContext();
var UserDispatchContext = React.createContext();

function userReducer(state, action) {
  switch (action.type) {
    case "LOGIN_SUCCESS":
      return { ...state, isAuthenticated: true, username: localStorage.getItem("username")};
    case "SIGN_OUT_SUCCESS":
      return { ...state, isAuthenticated: false, username: localStorage.getItem("username") };
    case "LOGIN_FAILURE":
      // TODO(RaresF): Show LOGIN ERROR MESSAGE
      return { ...state, isAuthenticated: false, username: localStorage.getItem("username") };
    default: {
      throw new Error(`Unhandled action type: ${action.type}`);
    }
  }
}

function UserProvider({ children }) {
  var [state, dispatch] = React.useReducer(userReducer, {
    isAuthenticated: !!localStorage.getItem("id_token"),
    username: localStorage.getItem("username"),
  });

  return (
    <UserStateContext.Provider value={state}>
      <UserDispatchContext.Provider value={dispatch}>
        {children}
      </UserDispatchContext.Provider>
    </UserStateContext.Provider>
  );
}

function useUserState() {
  var context = React.useContext(UserStateContext);
  if (context === undefined) {
    throw new Error("useUserState must be used within a UserProvider");
  }
  return context;
}

function useUserDispatch() {
  var context = React.useContext(UserDispatchContext);
  if (context === undefined) {
    throw new Error("useUserDispatch must be used within a UserProvider");
  }
  return context;
}


export { UserProvider, useUserState, useUserDispatch, loginUser, signOut };

// ###########################################################

async function loginUser(dispatch, login, password, history, setIsLoading, setError) {
  setError(false);
  setIsLoading(true);

  const authUrl = backend_login_ip + '/user/' + login + '/' + password;

  var authValid;
  await fetch(authUrl)
      .then(function (response) {
        return response.json();
      })
      .then(function (jsonResponse) {
        authValid = jsonResponse['authenticated'];
      });


  if (!!login && !!password && authValid === true) {
    setTimeout(() => {
      localStorage.setItem("id_token", "1");
      localStorage.setItem("username", login);
      dispatch({type: "LOGIN_SUCCESS"});
      setError(null);
      setIsLoading(false);

      history.push("/app/dashboard");
    }, 2000);
  } else {
    dispatch({type: "LOGIN_FAILURE"});
    setError(true);
    setIsLoading(false);
  }
}

function signOut(dispatch, history) {
  localStorage.removeItem("id_token");
  dispatch({ type: "SIGN_OUT_SUCCESS" });
  history.push("/login");
}
