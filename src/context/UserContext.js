import React from "react";

var UserStateContext = React.createContext();
var UserDispatchContext = React.createContext();

function userReducer(state, action) {
  switch (action.type) {
    case "LOGIN_SUCCESS":
      return { ...state, isAuthenticated: true };
    case "SIGN_OUT_SUCCESS":
      return { ...state, isAuthenticated: false };
    case "LOGIN_FAILURE":
      // TODO(RaresF): Show LOGIN ERROR MESSAGE
      return { ...state, isAuthenticated: false };
    default: {
      throw new Error(`Unhandled action type: ${action.type}`);
    }
  }
}

function UserProvider({ children }) {
  var [state, dispatch] = React.useReducer(userReducer, {
    isAuthenticated: !!localStorage.getItem("id_token"),
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

  const authUrl = 'http://109.103.170.75:31001/user/' + login + '/' + password;

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
      console.log(localStorage.getItem("username"));
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
