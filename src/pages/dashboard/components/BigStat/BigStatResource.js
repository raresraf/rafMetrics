import React, { useState } from "react";
import { Grid, Select, MenuItem, Input } from "@material-ui/core";
import { ArrowForward as ArrowForwardIcon } from "@material-ui/icons";
import { useTheme } from "@material-ui/styles";
import { BarChart, Bar } from "recharts";
import classnames from "classnames";

// styles
import useStyles from "./styles";

// components
import Widget from "../../../../components/Widget";
import { Typography } from "../../../../components/Wrappers";

export default function BigStatResource(props) {
  var { product, total, color, lowest, median, highest } = props;
  var classes = useStyles();
  var theme = useTheme();

  // local
  var [value, setValue] = useState("daily");

  return (
    <Widget
      header={
        <div className={classes.title}>
          <Typography variant="h5">{product}</Typography>

          <Select
            value={value}
            onChange={e => setValue(e.target.value)}
            input={
              <Input
                disableUnderline
                classes={{ input: classes.selectInput }}
              />
            }
            className={classes.select}
          >
            <MenuItem value="daily">Daily</MenuItem>
            <MenuItem value="weekly">Weekly</MenuItem>
            <MenuItem value="monthly">Monthly</MenuItem>
          </Select>
        </div>
      }
      upperTitle
    >
      <div className={classes.totalValueContainer}>
        <div className={classes.totalValue}>
          <Typography size="xxl" color="text" colorBrightness="secondary">
            {total[value]}
          </Typography>
          <Typography color={total.percent.profit ? "success" : "secondary"}>
            &nbsp;{total.percent.profit ? "+" : "-"}
            {total.percent.value}%
          </Typography>
        </div>
        <BarChart width={150} height={70} data={getRandomData()}>
          <Bar
            dataKey="value"
            fill={theme.palette[color].main}
            radius={10}
            barSize={10}
          />
        </BarChart>
      </div>
      <div className={classes.bottomStatsContainer}>
        <div className={classnames(classes.statCell, classes.borderRight)}>
          <Grid container alignItems="center">
            <Typography variant="h6">{lowest[value].value}</Typography>
            <ArrowForwardIcon
              className={classnames(classes.profitArrow, {
                [!lowest[value].profit]: classes.profitArrowDanger,
              })}
            />
          </Grid>
          <Typography size="sm" color="text" colorBrightness="secondary">
            Lowest response time
          </Typography>
        </div>
        <div className={classes.statCell}>
          <Grid container alignItems="center">
            <Typography variant="h6">{median[value].value}%</Typography>
            <ArrowForwardIcon
              className={classnames(classes.profitArrow, {
                [!lowest[value].profit]: classes.profitArrowDanger,
              })}
            />
          </Grid>
          <Typography size="sm" color="text" colorBrightness="secondary">
             Median response time
          </Typography>
        </div>
        <div className={classnames(classes.statCell, classes.borderRight)}>
          <Grid container alignItems="center">
            <Typography variant="h6">
              {highest[value].value}
            </Typography>
            <ArrowForwardIcon
              className={classnames(classes.profitArrow, {
                [classes.profitArrowDanger]: !highest[value].profit,
              })}
            />
          </Grid>
          <Typography size="sm" color="text" colorBrightness="secondary">
            Highest response time
          </Typography>
        </div>
      </div>
    </Widget>
  );
}

// #######################################################################

function getRandomData() {
  return Array(7)
    .fill()
    .map(() => ({ value: Math.floor(Math.random() * 10) + 1 }));
}
