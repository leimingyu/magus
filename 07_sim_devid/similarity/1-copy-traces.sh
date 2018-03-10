#!/bin/bash
if [ ! -d "metrics" ]; then
  mkdir -p metrics
fi

if [ ! -d "traces" ]; then
  mkdir -p traces 
fi

cp ../../apps/devid_cudasdk80/metrics/* ./metrics/
cp ../../apps/devid_cudasdk80/traces/* ./traces/

cp ../../apps/devid_lonestar/metrics/* ./metrics/
cp ../../apps/devid_lonestar/traces/* ./traces/

cp ../../apps/devid_parboil/metrics/* ./metrics/
cp ../../apps/devid_parboil/traces/* ./traces/

cp ../../apps/devid_poly/metrics/* ./metrics/
cp ../../apps/devid_poly/traces/* ./traces/

cp ../../apps/devid_rodinia/metrics/* ./metrics/
cp ../../apps/devid_rodinia/traces/* ./traces/

cp ../../apps/devid_shoc/metrics/* ./metrics/
cp ../../apps/devid_shoc/traces/* ./traces/



metrics_num=`ls metrics/ | wc -l`
traces_num=`ls traces/ | wc -l`

if [ "$metrics_num" = "$traces_num" ]; then
		echo "End of copying files. Looks good!"
else
		echo "Error! The number of metrics and traces files do not match!"
fi

