package botControl;
use strict;
use Globals qw( $char );
#Registra o nome do plugin
#register(nome_curto,nome_para_humanos,unload callback,reload callback)
my $hook = Plugins::addHooks(["base_level_changed" => \&onLevelUp],
                            ["AI_storage_done"=>\&onStorageDone],
                            ["disconnected"=>\&onDisconnect],
                            ["packet/inventory_item_added"=>\&onItem]);

sub on_unload(){
  Plugins::delHooks($hook);
}

sub on_reload(){
  &on_unload;
}

sub onItem{
  my ( undef, $args ) = @_;
  return if $args->{fail};
  my %item_array;
  for my $items (@{$char->inventory}){
          $item_array{$items->{name}} = $items->{amount};
  }
  system("python","/home/eduardo/botControl/log.py","3",$Settings::console_log_file,%item_array);
}

sub onStorageDone{
  if ($char->storage->wasOpenedThisSession()) {
    my (undef, $args) = @_;
    my %item_array;
    for my $items (@{$char->storage}){
      $item_array{$items->{name}} = $items->{amount};
    }
  system("python","/home/eduardo/botControl/log.py","0",$Settings::console_log_file,%item_array);
  }
}

sub onDisconnect{
  system("python","/home/eduardo/botControl/log.py","2",$Settings::console_log_file);
}

sub onLevelUp {
        my ( undef, $args ) = @_;
        return if $args->{fail};
        my %item_array;
        for my $items (@{$char->inventory}){
                $item_array{$items->{name}} = $items->{amount};
        }
        system("python","/home/eduardo/botControl/log.py","1",$Settings::console_log_file,$char->{'lv'},$char->{'lv_job'},%item_array);

}

1;
