export var backend_login_ip;
export var backend_webmonitoringapi_ip;

/* Configure FE
if(process.env.DOCKER_COMPOSE_BUILD) {
  // Docker Swarm
  backend_login_ip = "login:31001";
  backend_webmonitoringapi_ip = "webmonitoringapi:31002";
}
else {
  // K8s
  backend_login_ip = "http://109.103.170.75:31001";
  backend_webmonitoringapi_ip = "http://109.103.170.75:31002";
}
*/

var backend_ip = "http://ec2-18-130-104-21.eu-west-2.compute.amazonaws.com";
backend_login_ip = backend_ip + ":31001";
backend_webmonitoringapi_ip = backend_ip + ":31002";