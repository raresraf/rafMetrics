import React from 'react';
import {Drawer, IconButton, List, withStyles} from "@material-ui/core";
import {
  ArrowBack as ArrowBackIcon,
  FilterNone as UIElementsIcon,
  HelpOutline as FAQIcon,
  Home as HomeIcon,
  LibraryBooks as LibraryIcon, NetworkWifi as WifiIcon,
  QuestionAnswer as SupportIcon, Web as WebMonitoringIcon,
} from "@material-ui/icons";
import classNames from 'classnames';

import SidebarLink from './components/SidebarLink/SidebarLinkContainer';

const structure = [
  { id: 0, label: 'Dashboard', link: '/app/dashboard', icon: <HomeIcon /> },
  {
    id: 4,
    label: 'UI Elements',
    link: '/app/ui',
    icon: <UIElementsIcon />,
    children: [
      { label: 'Icons', link: '/app/ui/icons' },
    ],
  },
  {
    id: 5,
    label: "WebMonitoring",
    link: "/app/ui/",
    icon: <WifiIcon/>,
    children: [
      { label: "Resource", link: "/app/ui/resourcemanager" },
      { label: "Website", link: "/app/ui/websitemanager" },
    ],
  },
  {
    id: 6,
    label: "Statistics",
    link: "/app/ui",
    icon: <WebMonitoringIcon/>,
    children: [
      { label: "Resource", link: "/app/ui/resourcemanagerstatistics" },
      { label: "Website", link: "/app/ui/websitemanagerstatistics" },
    ],
  },
  { id: 7, type: 'divider' },
  { id: 8, type: 'title', label: 'HELP' },
  { id: 9, label: 'Library', link: '', icon: <LibraryIcon /> },
  { id: 10, label: 'Support', link: '', icon: <SupportIcon /> },
  { id: 11, label: 'FAQ', link: '', icon: <FAQIcon />},
  { id: 12, type: 'divider' },
];

const SidebarView = ({ classes, theme, toggleSidebar, isSidebarOpened, isPermanent, location }) => {
  return (
    <Drawer
      variant={isPermanent ? 'permanent' : 'temporary'}
      className={classNames(classes.drawer, {
        [classes.drawerOpen]: isSidebarOpened,
        [classes.drawerClose]: !isSidebarOpened,
      })}
      classes={{
        paper: classNames(classes.drawer, {
          [classes.drawerOpen]: isSidebarOpened,
          [classes.drawerClose]: !isSidebarOpened,
        }),
      }}
      open={isSidebarOpened}
    >
      <div className={classes.mobileBackButton}>
        <IconButton
          onClick={toggleSidebar}
        >
          <ArrowBackIcon classes={{ root: classNames(classes.headerIcon, classes.headerIconCollapse) }} />
        </IconButton>
      </div>
      <List className={classes.sidebarList}>
        {structure.map(link => <SidebarLink key={link.id} location={location} isSidebarOpened={isSidebarOpened} {...link} />)}
      </List>
    </Drawer>
  );
}

const drawerWidth = 240;

const styles = theme => ({
  menuButton: {
    marginLeft: 12,
    marginRight: 36,
  },
  hide: {
    display: 'none',
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0,
    whiteSpace: 'nowrap',
    top: theme.spacing.unit * 8,
    [theme.breakpoints.down("sm")]: {
      top: 0,
    }
  },
  drawerOpen: {
    width: drawerWidth,
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  drawerClose: {
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    overflowX: 'hidden',
    width: theme.spacing.unit * 7 + 40,
    [theme.breakpoints.down("sm")]: {
      width: drawerWidth,
    }
  },
  toolbar: {
    ...theme.mixins.toolbar,
    [theme.breakpoints.down("sm")]: {
      display: 'none',
    }
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing.unit * 3,
  },
  mobileBackButton: {
    marginTop: theme.spacing.unit * .5,
    marginLeft: theme.spacing.unit * 3,
    [theme.breakpoints.only("sm")]: {
      marginTop: theme.spacing.unit * .625,
    },
    [theme.breakpoints.up("md")]: {
      display: 'none',
    }
  }
});

export default withStyles(styles, { withTheme: true })(SidebarView);
