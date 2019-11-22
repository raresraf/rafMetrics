import React, {useState} from "react";
import {Grid, LinearProgress, MenuItem, OutlinedInput, Select,} from "@material-ui/core";
import {useTheme} from "@material-ui/styles";
import {Area, AreaChart, ComposedChart, Line, LineChart, ResponsiveContainer, XAxis, YAxis,} from "recharts";
// styles
import useStyles from "./styles";
// components
import mock from "./mock";
import Widget from "../../components/Widget";
import PageTitle from "../../components/PageTitle";
import {Typography} from "../../components/Wrappers";
import Dot from "../../components/Sidebar/components/Dot";
import TableResource from "./components/Table/TableResource";
import BigStatResource from "./components/BigStat/BigStatResource";
import {useUserState} from "../../context/UserContext";
import {useResourceState} from "../../context/ResourceContext";



export default function DashboardResourceStatistics(props) {
    var classes = useStyles();
    var theme = useTheme();
    return (
        <>
          <PageTitle title="Statistics Resource Manager"
          />
          <Grid container spacing={2}>
            <Grid item lg={6} md={6} sm={6} xs={12}>
              <Widget
                title="Last 24 hours"
                upperTitle
                bodyClass={classes.fullHeightBody}
                className={classes.card}
              >
                <div className={classes.visitsNumberContainer}>
                  <Typography size="xl" weight="medium">
                    12, 678
                  </Typography>
                  <LineChart
                    width={55}
                    height={30}
                    data={[
                      { value: 10 },
                      { value: 15 },
                      { value: 10 },
                      { value: 17 },
                      { value: 18 },
                    ]}
                    margin={{ left: theme.spacing(2) }}
                  >
                    <Line
                      type="natural"
                      dataKey="value"
                      stroke={theme.palette.success.main}
                      strokeWidth={2}
                      dot={false}
                    />
                  </LineChart>
                </div>
                <Grid
                  container
                  direction="row"
                  justify="space-between"
                  alignItems="center"
                >
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Requests
                    </Typography>
                    <Typography size="md">860</Typography>
                  </Grid>
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Average Time
                    </Typography>
                    <Typography size="md">32</Typography>
                  </Grid>
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Average Size
                    </Typography>
                    <Typography size="md">3.25%</Typography>
                  </Grid>
                </Grid>
              </Widget>
            </Grid>
            <Grid item lg={6} md={6} sm={6} xs={12}>
              <Widget
                title="All time"
                upperTitle
                bodyClass={classes.fullHeightBody}
                className={classes.card}
              >
                <div className={classes.visitsNumberContainer}>
                  <Typography size="xl" weight="medium">
                    12, 678
                  </Typography>
                  <LineChart
                    width={55}
                    height={30}
                    data={[
                      { value: 10 },
                      { value: 15 },
                      { value: 10 },
                      { value: 17 },
                      { value: 18 },
                    ]}
                    margin={{ left: theme.spacing(2) }}
                  >
                    <Line
                      type="natural"
                      dataKey="value"
                      stroke={theme.palette.success.main}
                      strokeWidth={2}
                      dot={false}
                    />
                  </LineChart>
                </div>
                <Grid
                  container
                  direction="row"
                  justify="space-between"
                  alignItems="center"
                >
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Requests
                    </Typography>
                    <Typography size="md">860</Typography>
                  </Grid>
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Average Time
                    </Typography>
                    <Typography size="md">32</Typography>
                  </Grid>
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Average Size
                    </Typography>
                    <Typography size="md">3.25%</Typography>
                  </Grid>
                </Grid>
              </Widget>
            </Grid>
          </Grid>



        </>
    );


}
