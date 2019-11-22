import React from "react";

var ResourceStateContext = React.createContext();
var ResourceDispatchContext = React.createContext();

function resourceReducer(state) {
  return { ...state, resourceid: localStorage.getItem("resourceid"),
  }
}

function ResourceProvider({ children }) {
  var [state, dispatch] = React.useReducer(resourceReducer, {
    resourceid: "1",
  });

  return (
    <ResourceStateContext.Provider value={state}>
      <ResourceDispatchContext.Provider value={dispatch}>
        {children}
      </ResourceDispatchContext.Provider>
    </ResourceStateContext.Provider>
  );
}

function useResourceState() {
  var context = React.useContext(ResourceStateContext);
  if (context === undefined) {
    throw new Error("useResourceState must be used within a ResourceStateContext");
  }
  return context;
}

function useResourceDispatch() {
  var context = React.useContext(ResourceDispatchContext);
  if (context === undefined) {
    throw new Error("useResourceDispatch must be used within a ResourceDispatchContext");
  }
  return context;
}


export { ResourceProvider, useResourceState, useResourceDispatch, updateResource};

function updateResource(resourceid, dispatch){
  localStorage.setItem("resourceid", resourceid);

  //window.location.reload();
  dispatch();
}