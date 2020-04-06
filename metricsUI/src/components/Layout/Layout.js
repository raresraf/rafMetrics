import React from "react";
import {Redirect, Route, Switch, withRouter,} from "react-router-dom";
import classnames from "classnames";
// styles
import useStyles from "./styles";
// components
import Header from "../Header";
import Sidebar from "../Sidebar";
// pages
import Dashboard from "../../pages/dashboard";
import DashboardResource from "../../pages/dashboard/DashboardResource";
import DashboardWebsite from "../../pages/dashboard/DashboardWebsite";
import DashboardResourceStatistics from "../../pages/dashboard/DashboardResourceStatistics";
import DashboardWebsiteStatistics from "../../pages/dashboard/DashboardWebsiteStatistics";
import Icons from "../../pages/icons";
// context
import {useLayoutState} from "../../context/LayoutContext";

function Layout(props) {
  var classes = useStyles();

  // global
  var layoutState = useLayoutState();

  return (
    <div className={classes.root}>
        <>
          <Header history={props.history} />
          <Sidebar />
          <div
            className={classnames(classes.content, {
              [classes.contentShift]: layoutState.isSidebarOpened,
            })}
          >
            <div className={classes.fakeToolbar} />
            <Switch>
              <Route path="/app/dashboard" component={Dashboard} />
              <Route
                exact
                path="/app/ui"
                render={() => <Redirect to="/app/ui/icons" />}
              />
              <Route path="/app/ui/icons" component={Icons} />
              <Route path="/app/ui/resourcemanager" component={DashboardResource} />
              <Route path="/app/ui/resourcemanagerstatistics" component={DashboardResourceStatistics} />
              <Route path="/app/ui/websitemanager" component={DashboardWebsite} />
              <Route path="/app/ui/websitemanagerstatistics" component={DashboardWebsiteStatistics} />

            </Switch>
          </div>
        </>
    </div>
  );
}

export default withRouter(Layout);
