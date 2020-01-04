import React from "react";
import {Button} from "@material-ui/core";
import {
  AccountBox as CustomerIcon,
  BusinessCenter as DeliveredIcon,
  DiscFull as DiscIcon,
  Done as ShippedIcon,
  Email as MessageIcon,
  Error as DefenceIcon,
  LocalOffer as TicketIcon,
  NotificationsNone as NotificationsIcon,
  Publish as UploadIcon,
  Report as ReportIcon,
  ShoppingCart as ShoppingCartIcon,
  SmsFailed as FeedbackIcon,
  ThumbUp as ThumbUpIcon,
} from "@material-ui/icons";
import {useTheme} from "@material-ui/styles";
import classnames from "classnames";
import tinycolor from "tinycolor2";
// styles
import useStyles from "./styles";
// components
import {Typography} from "../Wrappers";

const typesIcons = {
  "e-commerce": <ShoppingCartIcon />,
  notification: <NotificationsIcon />,
  offer: <TicketIcon />,
  info: <ThumbUpIcon />,
  message: <MessageIcon />,
  feedback: <FeedbackIcon />,
  customer: <CustomerIcon />,
  shipped: <ShippedIcon />,
  delivered: <DeliveredIcon />,
  defence: <DefenceIcon />,
  report: <ReportIcon />,
  upload: <UploadIcon />,
  disc: <DiscIcon />,
};

export default function Notification({ variant, ...props }) {
  var classes = useStyles();
  var theme = useTheme();

  const icon = getIconByType(props.type);
  const iconWithStyles = React.cloneElement(icon, {
    classes: {
      root: classes.notificationIcon,
    },
    style: {
      color:
        variant !== "contained" &&
        theme.palette[props.color] &&
        theme.palette[props.color].main,
    },
  });

  return (
    <div
      className={classnames(classes.notificationContainer, props.className, {
        [classes.notificationContained]: variant === "contained",
        [classes.notificationContainedShadowless]: props.shadowless,
      })}
      style={{
        backgroundColor:
          variant === "contained" &&
          theme.palette[props.color] &&
          theme.palette[props.color].main,
      }}
    >
      <div
        className={classnames(classes.notificationIconContainer, {
          [classes.notificationIconContainerContained]: variant === "contained",
          [classes.notificationIconContainerRounded]: variant === "rounded",
        })}
        style={{
          backgroundColor:
            variant === "rounded" &&
            theme.palette[props.color] &&
            tinycolor(theme.palette[props.color].main)
              .setAlpha(0.15)
              .toRgbString(),
        }}
      >
        {iconWithStyles}
      </div>
      <div className={classes.messageContainer}>
        <Typography
          className={classnames({
            [classes.containedTypography]: variant === "contained",
          })}
          variant={props.typographyVariant}
          size={variant !== "contained" && !props.typographyVariant && "md"}
        >
          {props.message}
        </Typography>
        {props.extraButton && props.extraButtonClick && (
          <Button
            onClick={props.extraButtonClick}
            disableRipple
            className={classes.extraButton}
          >
            {props.extraButton}
          </Button>
        )}
      </div>
    </div>
  );
}

// ####################################################################
function getIconByType(type = "offer") {
  return typesIcons[type];
}
