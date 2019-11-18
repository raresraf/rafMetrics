import React, { useState } from "react";
import {
  Grid,
  LinearProgress,
  Select,
  OutlinedInput,
  MenuItem,
} from "@material-ui/core";
import { useTheme } from "@material-ui/styles";
import {
  ResponsiveContainer,
  ComposedChart,
  AreaChart,
  LineChart,
  Line,
  Area,
  PieChart,
  Pie,
  Cell,
  YAxis,
  XAxis,
} from "recharts";

// styles
import useStyles from "./styles";

// components
import mock from "./mock";
import Widget from "../../components/Widget";
import PageTitle from "../../components/PageTitle";
import { Typography } from "../../components/Wrappers";
import Dot from "../../components/Sidebar/components/Dot";
import Table from "./components/Table/Table";
import TableResource from "./components/Table/TableResource";
import BigStat from "./components/BigStat/BigStat";
import BigStatResource from "./components/BigStat/BigStatResource";

const mainChartData = getMainChartData();
const PieChartData = [
  { name: "Group A", value: 400, color: "primary" },
  { name: "Group B", value: 300, color: "secondary" },
  { name: "Group C", value: 300, color: "warning" },
  { name: "Group D", value: 200, color: "success" },
];

function getAvailableResources() {
  return new Promise((resolve, reject) => {
    let availableResourcesUrl = "http://109.103.170.75:31002/availableResources/TestUsername";
    fetch(availableResourcesUrl)
        .then((response) => {
          return response.json();
        })
        .then((jsonResponse) => {
          resolve(jsonResponse);
        })
        .catch((err) => {
          reject(err);
        });
  })
}

function getRequestTime() {
  return new Promise((resolve, reject) => {
    let availableResourcesUrl = "http://109.103.170.75:31002/request_time/1";
    fetch(availableResourcesUrl)
        .then((response) => {
          return response.json();
        })
        .then((jsonResponse) => {
          resolve(jsonResponse);
        })
        .catch((err) => {
          reject(err);
        });
  })
}

var getAvailableResourcesLoaded = false;
var getRequestTimeLoaded = false;

export default function DashboardResource(props) {
  var classes = useStyles();
  var theme = useTheme();
  // local
  const [tableResource, setTableResource] = useState(mock.tableResource);
  const [bigStatResource, setBigStatResource] = useState(mock.bigStatResource);

  var [mainChartState, setMainChartState] = useState("monthly");

  if(!getAvailableResourcesLoaded)
    getAvailableResources().then(res => {
      setTableResource(res);
      getAvailableResourcesLoaded = true;
      console.log(res);
      console.log(mock.tableResource);
    });

  if(!getRequestTimeLoaded)
    getRequestTime().then(res => {
      setBigStatResource(res);
      getRequestTimeLoaded = true;
      console.log(res);
      console.log(mock.bigStatResource);
    });



    return (
        <>
          <PageTitle title="Dashboard Resources" button="See all resources" />
          <Grid container spacing={4}>
            <Grid item xs={12}>
              <Widget
                  title="Choose Resourse"
                  upperTitle
                  noBodyPadding
                  bodyClass={classes.tableWidget}
              >
                <TableResource data={tableResource} />
              </Widget>
            </Grid>


            <Grid item xs={12}>
              <Widget
                  bodyClass={classes.mainChartBody}
                  header={
                    <div className={classes.mainChartHeader}>
                      <Typography
                          variant="h5"
                          color="text"
                          colorBrightness="secondary"
                      >
                        Daily Line Chart
                      </Typography>
                      <div className={classes.mainChartHeaderLabels}>
                        <div className={classes.mainChartHeaderLabel}>
                          <Dot color="warning" />
                          <Typography className={classes.mainChartLegentElement}>
                            Tablet
                          </Typography>
                        </div>
                        <div className={classes.mainChartHeaderLabel}>
                          <Dot color="primary" />
                          <Typography className={classes.mainChartLegentElement}>
                            Mobile
                          </Typography>
                        </div>
                        <div className={classes.mainChartHeaderLabel}>
                          <Dot color="primary" />
                          <Typography className={classes.mainChartLegentElement}>
                            Desktop
                          </Typography>
                        </div>
                      </div>
                      <Select
                          value={mainChartState}
                          onChange={e => setMainChartState(e.target.value)}
                          input={
                            <OutlinedInput
                                labelWidth={0}
                                classes={{
                                  notchedOutline: classes.mainChartSelectRoot,
                                  input: classes.mainChartSelect,
                                }}
                            />
                          }
                          autoWidth
                      >
                        <MenuItem value="daily">Daily</MenuItem>
                        <MenuItem value="weekly">Weekly</MenuItem>
                        <MenuItem value="monthly">Monthly</MenuItem>
                      </Select>
                    </div>
                  }
              >
                <ResponsiveContainer width="100%" minWidth={500} height={350}>
                  <ComposedChart
                      margin={{ top: 0, right: -15, left: -15, bottom: 0 }}
                      data={mainChartData}
                  >
                    <YAxis
                        ticks={[0, 2500, 5000, 7500]}
                        tick={{ fill: theme.palette.text.hint + "80", fontSize: 14 }}
                        stroke={theme.palette.text.hint + "80"}
                        tickLine={false}
                    />
                    <XAxis
                        tickFormatter={i => i + 1}
                        tick={{ fill: theme.palette.text.hint + "80", fontSize: 14 }}
                        stroke={theme.palette.text.hint + "80"}
                        tickLine={false}
                    />
                    <Area
                        type="natural"
                        dataKey="desktop"
                        fill={theme.palette.background.light}
                        strokeWidth={0}
                        activeDot={false}
                    />
                    <Line
                        type="natural"
                        dataKey="mobile"
                        stroke={theme.palette.primary.main}
                        strokeWidth={2}
                        dot={false}
                        activeDot={false}
                    />
                    <Line
                        type="linear"
                        dataKey="tablet"
                        stroke={theme.palette.warning.main}
                        strokeWidth={2}
                        dot={{
                          stroke: theme.palette.warning.dark,
                          strokeWidth: 2,
                          fill: theme.palette.warning.main,
                        }}
                    />
                  </ComposedChart>
                </ResponsiveContainer>
              </Widget>
            </Grid>
            {bigStatResource.map(stat => (
                <Grid item md={4} sm={6} xs={12} key={stat.product}>
                  <BigStatResource {...stat} />
                </Grid>
            ))}
          </Grid>
        </>
    );


}

// #######################################################################
function getRandomData(length, min, max, multiplier = 10, maxDiff = 10) {
  var array = new Array(length).fill();
  let lastValue;

  return array.map((item, index) => {
    let randomValue = Math.floor(Math.random() * multiplier + 1);

    while (
        randomValue <= min ||
        randomValue >= max ||
        (lastValue && randomValue - lastValue > maxDiff)
        ) {
      randomValue = Math.floor(Math.random() * multiplier + 1);
    }

    lastValue = randomValue;

    return { value: randomValue };
  });
}

function getMainChartData() {
  var resultArray = [];
  var tablet = getRandomData(31, 3500, 6500, 7500, 1000);
  var desktop = getRandomData(31, 1500, 7500, 7500, 1500);
  var mobile = getRandomData(31, 1500, 7500, 7500, 1500);

  for (let i = 0; i < tablet.length; i++) {
    resultArray.push({
      tablet: tablet[i].value,
      desktop: desktop[i].value,
      mobile: mobile[i].value,
    });
  }

  return resultArray;
}