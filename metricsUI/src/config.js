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

backend_login_ip = "http://ec2-35-177-95-31.eu-west-2.compute.amazonaws.com:31001";
backend_webmonitoringapi_ip = "http://ec2-35-177-95-31.eu-west-2.compute.amazonaws.com:31002";