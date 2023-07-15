

import requests
import logging
import speedtest

import lucy
from lucy.utils.startup import internet_connectivity_check


class InternetSkills:

    @classmethod
    def run_speedtest(cls, **kwargs):
        """
        Run an internet speed test. Speed test will show
        1) Download Speed
        2) Upload Speed
        3) Ping
        """
        try:
            lucy.output_engine.respond("Sure! wait a second to measure")
            st = speedtest.Speedtest()
            server_names = []
            st.get_servers(server_names)

            downlink_bps = st.download()
            uplink_bps = st.upload()
            ping = st.results.ping
            up_mbps = uplink_bps / 1000000
            down_mbps = downlink_bps / 1000000

            lucy.output_engine.respond("Speedtest results:\n"
                         "The ping is: %s ms \n"
                         "The upling is: %0.2f Mbps \n"
                         "The downling is: %0.2f Mbps" % (ping, up_mbps, down_mbps)
                         )

        except Exception as e:
            lucy.output_engine.respond("I coudn't run a speedtest")
            logging.error("Speedtest error with message: {0}".format(e))

    @classmethod
    def internet_availability(cls,subject=None, **kwargs):
        """
        Tells to the user is the internet is available or not.
        """
        if internet_connectivity_check():
            lucy.output_engine.respond("The internet connection is ok")
            return True
        else:
            lucy.output_engine.respond("The internet is down for now")
            return False
