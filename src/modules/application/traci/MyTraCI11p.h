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

#ifndef MYTRACI11P_H_
#define MYTRACI11P_H_

#include "BaseWaveApplLayer.h"
#include "modules/mobility/traci/TraCIMobility.h"

using Veins::TraCIMobility;
using Veins::AnnotationManager;

/**
 * Small IVC Demo using 11p
 */
class MyTraCI11p : public BaseWaveApplLayer {
    public:
        virtual void initialize(int stage);
//        virtual void receiveSignal(cComponent* source, simsignal_t signalID, cObject* obj);

        enum WaveApplMessageKinds {
            SERVICE_PROVIDER = LAST_BASE_APPL_MESSAGE_KIND,
            TIMER_ALIVE
        };
    protected:
//        TraCIMobility* traci;
//        AnnotationManager* annotations;
//        simtime_t lastDroveAt;
//        bool sentMessage;
//        bool isParking;
//        bool sendWhileParking;
//        static const simsignalwrap_t parkingStateChangedSignal;
    protected:
        virtual void onBeacon(WaveShortMessage* wsm);
        virtual void onData(WaveShortMessage* wsm);
        void sendMessage(std::string blockedRoadId);
        virtual void handleSelfMsg(cMessage* msg);
//        virtual void handlePositionUpdate(cObject* obj);
//        virtual void handleParkingUpdate(cObject* obj);
        virtual void sendWSM(WaveShortMessage* wsm);
        cMessage* T_Alive;
};

#endif /* MYTRACI11P_H_ */
