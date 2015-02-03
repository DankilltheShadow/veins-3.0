//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see http://www.gnu.org/licenses/.
//

#include "application/traci/MyTraCI11p.h"

using Veins::TraCIMobilityAccess;
using Veins::AnnotationManagerAccess;

//const simsignalwrap_t MyTraCI11p::parkingStateChangedSignal = simsignalwrap_t(TRACI_SIGNAL_PARKING_CHANGE_NAME);

Define_Module(MyTraCI11p);

void MyTraCI11p::initialize(int stage) {
    BaseWaveApplLayer::initialize(stage);
    if (stage==0) {
        T_Alive = new cMessage("Internal Timer", TIMER_ALIVE);
        //simulate asynchronous channel access
        double in_offSet = dblrand() * (par("BeaconIntervalFN").doubleValue()/2);
        in_offSet = in_offSet + floor(in_offSet/0.050)*0.050;

        scheduleAt(simTime() + in_offSet, T_Alive);
    }
}

void MyTraCI11p::handleSelfMsg(cMessage* msg) {
    switch (msg->getKind()) {
        case TIMER_ALIVE: {
            t_channel channel = dataOnSch ? type_SCH : type_CCH;
            sendWSM(prepareWSM("I'm Alive", dataLengthBits, channel, dataPriority, 0, -2));
            scheduleAt(simTime() + par("AliveIntervalFN").doubleValue(), T_Alive);
            break;
        }
        default: {
            if (msg)
                DBG << "APP: Error: Got Self Message of unknown kind! Name: " << msg->getName() << endl;
            break;
        }
    }
}

void MyTraCI11p::onBeacon(WaveShortMessage* wsm) {
}

void MyTraCI11p::onData(WaveShortMessage* wsm) {
    /*findHost()->getDisplayString().updateWith("r=16,green");
    annotations->scheduleErase(1, annotations->drawLine(wsm->getSenderPos(), traci->getPositionAt(simTime()), "blue"));

    if (traci->getRoadId()[0] != ':') traci->commandChangeRoute(wsm->getWsmData(), 9999);
    if (!sentMessage) sendMessage(wsm->getWsmData());*/
}

void MyTraCI11p::sendMessage(std::string blockedRoadId) {
    /*sentMessage = true;

    t_channel channel = dataOnSch ? type_SCH : type_CCH;
    WaveShortMessage* wsm = prepareWSM("data", dataLengthBits, channel, dataPriority, -1,2);
    wsm->setWsmData(blockedRoadId.c_str());
    sendWSM(wsm);*/
}


//void MyTraCI11p::receiveSignal(cComponent* source, simsignal_t signalID, cObject* obj) {
////    Enter_Method_Silent();
////    if (signalID == mobilityStateChangedSignal) {
////        handlePositionUpdate(obj);
////    }
////    else if (signalID == parkingStateChangedSignal) {
////        handleParkingUpdate(obj);
////    }
//}
//void MyTraCI11p::handleParkingUpdate(cObject* obj) {
//    isParking = traci->getParkingState();
//    if (sendWhileParking == false) {
//        if (isParking == true) {
//            (FindModule<BaseConnectionManager*>::findGlobalModule())->unregisterNic(this->getParentModule()->getSubmodule("nic"));
//        }
//        else {
//            Coord pos = traci->getCurrentPosition();
//            (FindModule<BaseConnectionManager*>::findGlobalModule())->registerNic(this->getParentModule()->getSubmodule("nic"), (ChannelAccess*) this->getParentModule()->getSubmodule("nic")->getSubmodule("phy80211p"), &pos);
//        }
//    }
//}
//void MyTraCI11p::handlePositionUpdate(cObject* obj) {
//    BaseWaveApplLayer::handlePositionUpdate(obj);
//
//    // stopped for for at least 10s?
//    if (traci->getSpeed() < 1) {
//        if (simTime() - lastDroveAt >= 10) {
//            findHost()->getDisplayString().updateWith("r=16,red");
//            if (!sentMessage) sendMessage(traci->getRoadId());
//        }
//    }
//    else {
//        lastDroveAt = simTime();
//    }
//}
void MyTraCI11p::sendWSM(WaveShortMessage* wsm) {
//    if (isParking && !sendWhileParking) return;
//    sendDelayedDown(wsm,individualOffset);
}

