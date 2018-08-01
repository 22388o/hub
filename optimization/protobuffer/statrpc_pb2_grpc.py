# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

import protobuffer.statrpc_pb2 as statrpc__pb2


class GetStatisticsStub(object):
  """GetStatistics grpc service is used to make available hub statistical data.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetStatParams = channel.unary_unary(
        '/statrpc.GetStatistics/GetStatParams',
        request_serializer=statrpc__pb2.GetStatParamsRequest.SerializeToString,
        response_deserializer=statrpc__pb2.GetStatParamsResponse.FromString,
        )


class GetStatisticsServicer(object):
  """GetStatistics grpc service is used to make available hub statistical data.
  """

  def GetStatParams(self, request, context):
    """GetStatParams is used to get hub statistical patrameters.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GetStatisticsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetStatParams': grpc.unary_unary_rpc_method_handler(
          servicer.GetStatParams,
          request_deserializer=statrpc__pb2.GetStatParamsRequest.FromString,
          response_serializer=statrpc__pb2.GetStatParamsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'statrpc.GetStatistics', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
